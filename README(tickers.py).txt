Historical Stock Price Data Retrieval


This Python script retrieves historical stock price data for a list of tickers provided in a CSV file and saves the collected data in a CSV file. The script uses the yfinance library to download the data and pandas for data manipulation.

Requirements
Python 3
pandas
yfinance

Usage
Install the required libraries if not already installed:


pip install pandas yfinance

1. Download a list of tickers and save it as 'all_data.csv'. This file should only contain one column named 'Symbol' with the tickers.
2. Run the script:

python tickers.py


The script will:
1.Load the list of tickers from 'all_data.csv'.
2.Define the start and end dates for the data retrieval (start date is set to '2023-11-01', end date is set to '2024-03-07').
3.Initialize an empty DataFrame to store the data for all tickers.
4.Retrieve historical data for each ticker using yfinance and append it to the DataFrame.
5.Save the entire DataFrame containing historical data for all tickers to 'all_data.csv'.

Output

After running the script, a CSV file containing the historical data for all tickers will be saved as 'all_data.csv'. This file will have columns such as 'Open', 'High', 'Low', 'Close', 'Volume', and 'Date', along with a 'Symbol' column containing the ticker symbols.

Please note that the data retrieved is based on the specified start and end dates. To obtain data for a different time period, update the start_date and end_date variables accordingly.