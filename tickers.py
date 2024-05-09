import pandas as pd
import yfinance as yf

# Load the list of tickers from a CSV file
tickers = pd.read_csv('all_data.csv')['Symbol'].tolist()

# Define the start and end dates for the data
start_date = '2023-11-01'
end_date = '2024-03-07'

# Initialize an empty DataFrame to store the data for all tickers
all_data = pd.DataFrame()

# Retrieve the data for each ticker and append it to the DataFrame
for ticker in tickers:
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        data['Symbol'] = ticker  # Add a column for the ticker symbol
        all_data = all_data.append(data)
    except Exception as e:
        print(f"Could not download data for {ticker}: {e}")

# Save the DataFrame to a CSV file
all_data.to_csv('all_data.csv')