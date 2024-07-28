# Import necessary libraries
import pandas as pd
import numpy as np
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from io import BytesIO
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Set up logging to track the script's progress and any errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the URL of the website we'll be scraping
BASE_URL = 'https://coinmarketcap.com/'

def setup_driver():
    """
    Set up and configure the Chrome web driver for web scraping.
    This function creates a headless browser, which means it runs in the background without opening a visible window.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def safe_get_text(element):
    """
    Safely extract text from a web element, returning an empty string if the element doesn't exist.
    This helps prevent errors when trying to read data from the webpage.
    """
    return element.text.strip() if element else ''

def wait_for_page_load(driver, timeout=30):
    """
    Wait for the webpage to fully load before proceeding.
    This ensures we don't try to scrape data before it's available on the page.
    """
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

def scrape_main_page(driver):
    """
    Scrape cryptocurrency data from the main page of CoinMarketCap.
    This function extracts information like rank, name, price, and market cap for each listed cryptocurrency.
    """
    # Wait for the table containing cryptocurrency data to load
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table tbody tr')))
    
    rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    data = []
    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, 'td')
            if len(cols) >= 10:
                # Extract various data points for each cryptocurrency
                volume_elements = cols[8].find_elements(By.TAG_NAME, 'p')
                volume_24h = safe_get_text(volume_elements[0]) if volume_elements else ''
                volume_market_cap = safe_get_text(volume_elements[1]) if len(volume_elements) > 1 else ''
                
                data.append({
                    'Rank': int(safe_get_text(cols[1])),
                    'Name': safe_get_text(cols[2].find_element(By.CSS_SELECTOR, 'p[color="text"]')),
                    'Symbol': safe_get_text(cols[2].find_element(By.CSS_SELECTOR, 'p[color="text3"]')),
                    'Price': safe_get_text(cols[3].find_element(By.TAG_NAME, 'span')),
                    '1h %': safe_get_text(cols[4]),
                    '24h %': safe_get_text(cols[5]),
                    '7d %': safe_get_text(cols[6]),
                    'Market Cap': safe_get_text(cols[7]),
                    'Volume(24h)': volume_24h,
                    'Volume/Market Cap': volume_market_cap,
                    'Circulating Supply': safe_get_text(cols[9])
                })
        except Exception as e:
            logging.warning(f"Error scraping row: {str(e)}")
    
    logging.info(f"Scraped {len(data)} rows from the main page")
    return data

def scrape_coinmarketcap():
    """
    Main function to scrape data from CoinMarketCap.
    This function sets up the web driver, navigates to the website, and collects the cryptocurrency data.
    """
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_page_load(driver)
        data = scrape_main_page(driver)
        return pd.DataFrame(data).sort_values('Rank')
    except Exception as e:
        logging.error(f"Error scraping data: {str(e)}")
        return pd.DataFrame()
    finally:
        driver.quit()

def preprocess_data(df):
    """
    Clean and preprocess the scraped data.
    This function converts string values to numerical data and standardizes percentage values.
    """
    for col in ['Price', 'Market Cap', 'Volume(24h)']:
        df[col] = df[col].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    for col in ['1h %', '24h %', '7d %']:
        df[col] = df[col].str.rstrip('%').astype(float) / 100
    return df

def create_bar_plot(data, x, y, title, xlabel, ylabel):
    """
    Create a bar plot visualization of cryptocurrency data.
    This function is used to generate various charts for the analysis.
    """
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=x, y=y, data=data)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return plt.gcf()

def analyze_top_cryptocurrencies(df, top_n=10):
    """
    Perform in-depth analysis on the top cryptocurrencies.
    This function generates various statistics, correlations, and visualizations to provide insights into the cryptocurrency market.
    """
    top_cryptos = df.nlargest(top_n, 'Market Cap')
    
    # Generate summary statistics
    summary = top_cryptos[['Name', 'Price', 'Market Cap', '24h %', '7d %']].set_index('Name')
    
    # Calculate risk-reward metrics
    risk_reward = pd.DataFrame({
        'Name': top_cryptos['Name'],
        'Potential Reward (7d % Change)': top_cryptos['7d %'],
        'Risk (Price Volatility)': top_cryptos['24h %'].abs()
    }).set_index('Name')
    
    # Compute correlation matrix
    correlation = top_cryptos[['Price', 'Market Cap', 'Volume(24h)', '1h %', '24h %', '7d %']].corr()
    
    # Calculate additional metrics
    top_cryptos['Volume/Market Cap Ratio'] = top_cryptos['Volume(24h)'] / top_cryptos['Market Cap']
    top_cryptos['Volatility Index'] = (top_cryptos['24h %'].abs() + top_cryptos['7d %'].abs()) / 2
    
    # Perform statistical tests
    price_corr, _ = stats.pearsonr(top_cryptos['Price'], top_cryptos['Market Cap'])
    volume_corr, _ = stats.pearsonr(top_cryptos['Volume(24h)'], top_cryptos['Market Cap'])
    
    # Generate visualizations
    figs = {}
    figs['price_comparison'] = create_bar_plot(top_cryptos, 'Name', 'Price', 
                                               f"Price Comparison of Top {top_n} Cryptocurrencies",
                                               "Cryptocurrency", "Price ($)")
    figs['24h_change'] = create_bar_plot(top_cryptos, 'Name', '24h %', 
                                         f"24-hour Change Comparison of Top {top_n} Cryptocurrencies",
                                         "Cryptocurrency", "24-hour Change (%)")
    
    plt.figure(figsize=(10, 10))
    plt.pie(top_cryptos['Market Cap'], labels=top_cryptos['Name'], autopct='%1.1f%%')
    plt.title(f"Market Dominance of Top {top_n} Cryptocurrencies")
    plt.axis('equal')
    figs['market_dominance'] = plt.gcf()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Heatmap of Top Cryptocurrency Metrics")
    figs['correlation_heatmap'] = plt.gcf()
    
    figs['volume_market_cap_ratio'] = create_bar_plot(top_cryptos, 'Name', 'Volume/Market Cap Ratio', 
                                                      f"Volume to Market Cap Ratio of Top {top_n} Cryptocurrencies",
                                                      "Cryptocurrency", "Volume/Market Cap Ratio")
    
    price_changes = top_cryptos[['Name', '1h %', '24h %', '7d %']]
    price_changes_melted = price_changes.melt(id_vars=['Name'], var_name='Time Period', value_name='Price Change')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Name', y='Price Change', hue='Time Period', data=price_changes_melted)
    plt.title(f"Normalized Price Change Comparison of Top {top_n} Cryptocurrencies")
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Price Change (%)")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Time Period')
    plt.tight_layout()
    figs['normalized_price_change'] = plt.gcf()
    
    return summary, risk_reward, correlation, top_cryptos, price_corr, volume_corr, figs

def save_to_excel(df, analysis_results, filename='crypto_analysis.xlsx'):
    """
    Save all analysis results to an Excel file.
    This function creates a comprehensive report with multiple sheets containing different aspects of the analysis.
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Raw Data', index=False)
        analysis_results[0].to_excel(writer, sheet_name='Summary')
        analysis_results[1].to_excel(writer, sheet_name='Risk-Reward Analysis')
        analysis_results[2].to_excel(writer, sheet_name='Correlation')
        analysis_results[3].to_excel(writer, sheet_name='Top Cryptocurrencies', index=False)
        
        stats_df = pd.DataFrame({
            'Metric': ['Price-Market Cap Correlation', 'Volume-Market Cap Correlation'],
            'Value': [analysis_results[4], analysis_results[5]]
        })
        stats_df.to_excel(writer, sheet_name='Statistical Tests', index=False)
        
        # Save visualizations as images in the Excel file
        workbook = writer.book
        for name, fig in analysis_results[6].items():
            img_buffer = BytesIO()
            fig.savefig(img_buffer, format='png')
            img = Image(img_buffer)
            worksheet = workbook.create_sheet(title=name.replace('_', ' ').title())
            worksheet.add_image(img, 'A1')
    
    logging.info(f"Analysis results saved to {filename}")

def scrape_crypto_data(interval=3600):
    """
    Main function to periodically scrape cryptocurrency data and perform analysis.
    This function runs indefinitely, updating the data and analysis at regular intervals.
    """
    while True:
        start_time = time.time()
        df = scrape_coinmarketcap()
        end_time = time.time()
        
        if not df.empty:
            df = preprocess_data(df)
            logging.info(f"Data scraped successfully. Total rows: {len(df)}. Time taken: {end_time - start_time:.2f} seconds.")
            print(df.head().to_string(index=False))
            
            analysis_results = analyze_top_cryptocurrencies(df)
            save_to_excel(df, analysis_results)
            
            print("Analysis complete. Check the generated Excel file for results.")
        else:
            logging.warning("No data scraped. Skipping analysis and Excel save.")
        
        print(f"Next update in {interval} seconds. Press Ctrl+C to exit.")
        time.sleep(interval)

if __name__ == "__main__":
    scrape_crypto_data()
