import pandas as pd
import yfinance as yf
from datetime import datetime

# Load the list of S&P 500 tickers from a CSV file
sp500_tickers = pd.read_csv('all_data.csv')['Symbol'].tolist()

# Define the list of your current investments
current_investments = ['BNL', 'NTRS', 'MO', 'O', 'RTX', 'SCHD', 'FDVV', 'EPD', 'GLP', 'JEPQ', 'CSWC', 'CTSH']

# Remove the current investments from the list of S&P 500 tickers
tickers = [ticker for ticker in sp500_tickers if ticker not in current_investments]

# Combine the lists
all_tickers = tickers + current_investments

# Define the start and end dates for the data
start_date = '2023-11-01'
end_date = datetime.now().date()

# Initialize an empty DataFrame to store the data for all tickers
all_data = pd.DataFrame()

# Retrieve the data for each ticker and append it to the DataFrame
for i, ticker in enumerate(all_tickers, start=1):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Symbol'] = ticker  # Add a column for the ticker symbol
    all_data = all_data.append(data)

    # Print a progress message
    print(f'Processed {i} of {len(all_tickers)} tickers ({100 * i / len(all_tickers):.2f}% complete)')

# Calculate the total return for each ticker
total_returns = all_data.groupby('Symbol')['Close'].apply(lambda x: x.iloc[-1] / x.iloc[0] - 1)

# Get the total return for the S&P 500
sp500_return = total_returns.loc['^GSPC']

# Select the tickers that have a higher total return than the S&P 500
selected_tickers = total_returns[total_returns > sp500_return].index

print(selected_tickers)

# Save the DataFrame to a CSV file
all_data.to_csv('all_data.csv')