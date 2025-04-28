# 🌐 Web Data Insights Explorer

## Overview

Unlock the power of web data with the **Web Data Insights Explorer**! This user-friendly web application, built with Python and Flask, empowers you to effortlessly extract, analyze, and visualize information from any webpage. Whether you're gathering contact details, tracking keywords, or understanding online sentiment, this toolkit provides a comprehensive suite of features for all your web scraping and data analysis needs.

## ✨ Features

-   **🎯 Dynamic Web Scraping**: Extract diverse data types (emails, phone numbers, URLs, custom patterns) using flexible regex.
-   **😊 Sentiment Analysis**: Instantly gauge the sentiment of extracted text content.
-   **📊 Data Visualization**: Generate insightful charts, including sentiment distribution, word clouds, and more.
-   **💾 CSV Export**: Easily save extracted and analyzed data to CSV files for offline analysis or reporting.
-   **🖱️ User-Friendly Interface**: Simple web UI for entering URLs and selecting extraction options.
-   **🛡️ Ethical Scraping**: Automatically respects `robots.txt` rules for responsible data collection.
-   **⚡ Performance Optimized**: Leverages caching and multithreading for faster scraping and analysis.

## 🚀 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/tzolkowski96/web-data-insights-explorer.git
    cd web-data-insights-explorer
    ```

2.  Create and activate a virtual environment (recommended):
    ```bash
    # Ensure you have Python 3 installed
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    .\venv\Scripts\activate
    ```

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

1.  Run the Flask application from your terminal:
    ```bash
    python web_data_extractor.py
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:5000` (or the URL provided in the terminal).

3.  Enter the target URL you wish to scrape.

4.  Select the type of data to extract from the dropdown or provide your own custom regex pattern.

5.  Click "Scrape and Analyze".

6.  Explore the extracted data table, view the generated visualizations, and download the results as a CSV file or image.

## 🖼️ Demo / Screenshots

*(Consider adding a GIF or screenshots here to showcase the application in action!)*

Example:
`![Screenshot of Web Data Insights Explorer](link/to/your/screenshot.png)`

## 💻 Technologies Used

-   **Backend**: Python, Flask
-   **Web Scraping**: Requests, BeautifulSoup
-   **Data Handling**: Pandas
-   **NLP**: NLTK (SentimentIntensityAnalyzer)
-   **Visualization**: Matplotlib, Seaborn, WordCloud
-   **Concurrency**: concurrent.futures (ThreadPoolExecutor)
-   **Caching**: functools (lru_cache)

## 🙌 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/tzolkowski96/web-data-insights-explorer/issues) (if applicable) or submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For any queries or suggestions, please reach out via the [contact form on my portfolio website](https://tzolkowski96.github.io/portfolio/).
