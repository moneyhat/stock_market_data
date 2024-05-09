S&P 500 Ticker Analysis

This Python script analyzes historical stock price data for all tickers in the S&P 500 index and filters them based on their total return compared to the S&P 500 index return. The script uses the yfinance library to retrieve the data and pandas for data manipulation.


Requirements
Python 3
pandas
yfinance
Usage
Install the required libraries if not already installed:


pip install pandas yfinance

Download a list of all S&P 500 tickers and save it as 'all_data.csv'. This file should only contain one column named 'Symbol' with the tickers.

Define your current investment tickers in the current_investments variable.

Run the script:

python sp500_analysis.py

The script will:
Load the list of S&P 500 tickers from 'all_data.csv'.
Remove the current investments from the list of S&P 500 tickers.
Retrieve historical data for each ticker using yfinance and store it in a DataFrame.
Calculate the total return for each ticker.
Get the total return for the S&P 500 index.
Select the tickers with a higher total return than the S&P 500 index.
Print the selected tickers.
Save the entire DataFrame containing historical data for all tickers to 'all_data.csv'.

Output#
After running the script, you will get a list of tickers that have performed better than the S&P 500 index during the specified time period (start date to the current date) printed on the console. Additionally, a CSV file containing the historical data for all tickers will be saved as 'all_data.csv'.