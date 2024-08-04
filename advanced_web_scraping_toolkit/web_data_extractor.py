# Import necessary libraries
import requests
import re
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg for non-interactive plotting
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from urllib import robotparser
import ssl
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns
import os
from flask import Flask, render_template, request, send_file, abort
from werkzeug.utils import secure_filename
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

# Set up logging and SSL context
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
ssl._create_default_https_context = ssl._create_unverified_context

# Download necessary NLTK data
nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)

# Initialize the Robot parser
rp = robotparser.RobotFileParser()

# Define regex patterns for different types of data
regex_options = {
    "Email addresses": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "Phone numbers": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
    "URLs": r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    "Dates": r'\d{1,2}/\d{1,2}/\d{2,4}',
    "Prices": r'\$\d+(?:\.\d{2})?',
    "Social media handles": r'@[\w\d]+',
    "Hashtags": r'#[\w\d]+',
    "Named Entities": r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b',
    "Numerical Data": r'\b\d+(?:\.\d+)?\b',
    "Sentences": r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s',
    "Keywords": r'\b(important|significant|crucial|key)\s\w+\b',
    "HTML Tags": r'<[^>]+>',
    "All text": r'.*'
}

# Initialize Flask app and set configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

@lru_cache(maxsize=100)
def fetch_webpage(url):
    """
    Fetch the content of a webpage while respecting robots.txt rules.
    
    Args:
    url (str): The URL of the webpage to fetch.
    
    Returns:
    str: The HTML content of the webpage, or None if fetching fails.
    """
    # Check if scraping is allowed by robots.txt
    if not can_fetch(url):
        logging.warning(f"Robots.txt disallows scraping: {url}")
        return None

    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes
        response.raise_for_status()
        # Return the text content of the response
        return response.text
    except requests.RequestException as e:
        # Log any errors that occur during the request
        logging.error(f"Error fetching webpage: {e}")
        return None

def can_fetch(url):
    """
    Check if scraping is allowed for the given URL according to robots.txt rules.
    
    Args:
    url (str): The URL to check.
    
    Returns:
    bool: True if scraping is allowed, False otherwise.
    """
    # Set the URL for the robots.txt file
    rp.set_url(f"{url.split('/')[0]}//{url.split('/')[2]}/robots.txt")
    # Read the robots.txt file
    rp.read()
    # Check if scraping is allowed for the given URL
    return rp.can_fetch("*", url)

def parse_html(html_content):
    """
    Parse HTML content using BeautifulSoup.
    
    Args:
    html_content (str): The HTML content to parse.
    
    Returns:
    BeautifulSoup: A BeautifulSoup object representing the parsed HTML.
    """
    return BeautifulSoup(html_content, 'html.parser')

def extract_data(soup, pattern):
    """
    Extract data from parsed HTML using a regex pattern.
    
    Args:
    soup (BeautifulSoup): The parsed HTML.
    pattern (str): The regex pattern to use for extraction.
    
    Returns:
    list: A list of extracted data items.
    """
    # Find all tags that match the pattern and extract their text
    return [tag.text.strip() for tag in soup.find_all(['a', 'p', 'div', 'span']) if re.search(pattern, str(tag))]

def clean_data(data):
    """
    Clean the extracted data by removing special characters and extra whitespace.
    
    Args:
    data (list): The list of data items to clean.
    
    Returns:
    list: A list of cleaned data items.
    """
    # Remove special characters and convert to lowercase
    return [' '.join(re.sub(r'[^\w\s]', '', item.lower()).split()) for item in data]

@lru_cache(maxsize=1000)
def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    
    Args:
    text (str): The text to analyze.
    
    Returns:
    float: The compound sentiment score (-1 to 1).
    """
    # Initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    # Return the compound sentiment score
    return sia.polarity_scores(text)['compound']

def save_to_csv(data, filename):
    """
    Save the extracted and analyzed data to a CSV file.
    
    Args:
    data (list): The list of extracted data items.
    filename (str): The name of the CSV file to save.
    
    Returns:
    DataFrame: A pandas DataFrame containing the saved data.
    """
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=['Extracted Data'])
    # Clean the data and add additional analysis columns
    df['Cleaned Data'] = clean_data(df['Extracted Data'])
    df['Sentiment'] = df['Cleaned Data'].apply(analyze_sentiment)
    df['Word Count'] = df['Cleaned Data'].apply(lambda x: len(x.split()))
    df['Character Count'] = df['Cleaned Data'].apply(len)
    df['Uppercase Count'] = df['Extracted Data'].apply(lambda x: sum(1 for c in x if c.isupper()))
    df['Lowercase Count'] = df['Extracted Data'].apply(lambda x: sum(1 for c in x if c.islower()))
    df['Digit Count'] = df['Extracted Data'].apply(lambda x: sum(1 for c in x if c.isdigit()))
    
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Save the DataFrame to a CSV file
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    df.to_csv(full_path, index=False)
    logging.info(f"Data saved to {full_path}")
    return df

def visualize_data(df, filename):
    """
    Create visualizations of the analyzed data.
    
    Args:
    df (DataFrame): The pandas DataFrame containing the analyzed data.
    filename (str): The name of the file to save the visualization.
    
    Returns:
    str: The path to the saved visualization file.
    """
    # Create a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Sentiment Distribution
    sns.histplot(df['Sentiment'], kde=True, ax=axes[0, 0])
    axes[0, 0].set_title('Sentiment Distribution')
    axes[0, 0].set_xlabel('Sentiment Score')
    axes[0, 0].set_ylabel('Frequency')

    # Plot 2: Sentiment vs Word Count
    sns.scatterplot(x='Word Count', y='Sentiment', data=df, ax=axes[0, 1])
    axes[0, 1].set_title('Sentiment vs Word Count')
    axes[0, 1].set_xlabel('Word Count')
    axes[0, 1].set_ylabel('Sentiment Score')

    # Plot 3: Sentiment Categories Pie Chart
    df['Sentiment Category'] = pd.cut(df['Sentiment'], bins=[-1, -0.1, 0.1, 1], labels=['Negative', 'Neutral', 'Positive'])
    df['Sentiment Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axes[1, 0])
    axes[1, 0].set_title('Sentiment Categories')

    # Plot 4: Word Cloud
    text = ' '.join(df['Cleaned Data'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    axes[1, 1].imshow(wordcloud, interpolation='bilinear')
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Word Cloud')

    # Adjust layout and save the figure
    plt.tight_layout()
    plot_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    plt.savefig(plot_path, format='png')
    plt.close(fig)
    
    return plot_path

def scrape(url, pattern):
    """
    Scrape data from a webpage using the given pattern.
    
    Args:
    url (str): The URL of the webpage to scrape.
    pattern (str): The regex pattern to use for data extraction.
    
    Returns:
    list: A list of extracted data items.
    """
    # Fetch the webpage content
    html_content = fetch_webpage(url)
    if html_content:
        # Parse the HTML and extract data
        soup = parse_html(html_content)
        return extract_data(soup, pattern)
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle GET and POST requests to the main page of the web application.
    """
    if request.method == 'POST':
        # Get form data
        url = request.form['url']
        selected_option = request.form['regex_option']
        custom_regex = request.form['custom_regex']

        # Determine the pattern to use
        pattern = custom_regex if selected_option == "Custom Regex" and custom_regex else regex_options[selected_option]

        # Scrape data using a separate thread
        with ThreadPoolExecutor() as executor:
            future = executor.submit(scrape, url, pattern)
            data = future.result()

        if data:
            # Process and visualize the scraped data
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_data_{timestamp}.csv"
            df = save_to_csv(data, filename)
            plot_filename = f"plot_{timestamp}.png"
            plot_path = visualize_data(df, plot_filename)
            return render_template('index.html', regex_options=regex_options, results=df.to_html(classes='table table-striped'), plot_filename=plot_filename, csv_filename=filename)
        else:
            return render_template('index.html', regex_options=regex_options, error="No data was extracted. Please try a different URL or data type.")

    # For GET requests, just render the form
    return render_template('index.html', regex_options=regex_options)

@app.route('/download/<filename>')
def download_file(filename):
    """
    Handle requests to download CSV files.
    
    Args:
    filename (str): The name of the file to download.
    """
    try:
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)), as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/download_plot/<filename>')
def download_plot(filename):
    """
    Handle requests to download plot images.
    
    Args:
    filename (str): The name of the plot file to download.
    """
    try:
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)), as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle errors when the uploaded file is too large.
    """
    return 'File Too Large', 413

if __name__ == '__main__':
    app.run(debug=True)
