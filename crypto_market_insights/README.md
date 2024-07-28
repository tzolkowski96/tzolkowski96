# Crypto Market Insights

## Overview

This project contains a comprehensive cryptocurrency data pipeline that scrapes real-time data from CoinMarketCap, performs in-depth analysis, and generates insightful visualizations. It's designed to provide valuable market insights for cryptocurrency enthusiasts, analysts, and investors.

## Features

- Real-time data scraping from CoinMarketCap
- Detailed analysis of top cryptocurrencies
- Generation of various visualizations including price comparisons, market dominance, and correlation heatmaps
- Automated Excel report generation with raw data and analysis results
- Periodic data updates with customizable intervals

## Requirements

- Python 3.7+
- Selenium WebDriver
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- openpyxl

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tzolkowski96/crypto_market_insights.git
```
2. Navigate to the project directory:
```bash
cd crypto_market_insights
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using the following command:

```bash
python cryptocurrency_data_pipeline.py
```

The script will start scraping data, perform analysis, and generate an Excel report. It will continue to update at regular intervals until stopped.

## Output

The script generates an Excel file named 'crypto_analysis.xlsx' containing:

- Raw scraped data
- Summary statistics
- Risk-reward analysis
- Correlation matrix
- Detailed analysis of top cryptocurrencies
- Statistical tests results
- Visualizations as embedded images

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any queries or suggestions, please reach out through the [contact form on my portfolio website](https://tzolkowski96.github.io/portfolio/).
