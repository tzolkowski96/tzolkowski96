# Web Data Insights Explorer

## Overview

The Web Data Insights Explorer is a powerful, user-friendly web application designed to extract, analyze, and visualize data from web pages. Built using Python and Flask, this tool offers a comprehensive suite of features for web scraping, data processing, sentiment analysis, and data visualization.

## Features

- **Dynamic Web Scraping**: Extract various types of data (emails, phone numbers, URLs, etc.) using customizable regex patterns.
- **Sentiment Analysis**: Analyze the sentiment of extracted text data.
- **Data Visualization**: Generate insightful visualizations including sentiment distribution, word clouds, and more.
- **CSV Export**: Save extracted and analyzed data to CSV files for further analysis.
- **User-Friendly Interface**: Easy-to-use web interface for inputting URLs and selecting data types to extract.
- **Ethical Scraping**: Respects robots.txt rules to ensure ethical web scraping practices.
- **Performance Optimization**: Utilizes caching and multithreading for improved efficiency.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tzolkowski96/web-data-insights-explorer.git cd web-data-insights-explorer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python web_data_extractor.py
    ```

2. Open a web browser and navigate to `http://localhost:5000` or the URL provided by Flask (if different).

3. Enter a URL, select the type of data to extract (or enter a custom regex), and click "Scrape and Analyze".

4. View the results, download the CSV file, or explore the generated visualizations.

## Technologies Used

- Python
- Flask
- BeautifulSoup
- Pandas
- NLTK
- Matplotlib
- Seaborn
- WordCloud

## Contributing

Contributions to improve the Web Data Insights Explorer are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Contact

For any queries or suggestions, please reach out through the [contact form on my portfolio website](https://tzolkowski96.github.io/portfolio/).
