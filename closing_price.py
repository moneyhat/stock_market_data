import pandas as pd
import matplotlib.pyplot as plt


###########Normalized Closing Price Plot for Top Performing Stocks########

# Load the data from the CSV file
data = pd.read_csv('all_data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Normalize the closing prices by their initial price
data['Normalized Close'] = data.groupby('Symbol')['Close'].transform(lambda x: x / x.iloc[0])

# Get the final normalized closing price for each ticker
final_prices = data.groupby('Symbol')['Normalized Close'].last()

# Select the top 8 performing stocks (excluding '^GSPC')
top_stocks = final_prices.drop('^GSPC').nlargest(10).index

# Add '^GSPC' to the list of stocks to plot
stocks_to_plot = list(top_stocks) + ['^GSPC']

# Plot the normalized closing prices of the selected stocks
for ticker in stocks_to_plot:
    linewidth = 3.0 if ticker == '^GSPC' else 1.0
    data.loc[data['Symbol'] == ticker, 'Normalized Close'].plot(label=ticker, linewidth=linewidth)

plt.legend()
plt.title('Normalized Closing Prices Over Time for Top 8 Performing Stocks and ^GSPC')
plt.xlabel('Date')
plt.ylabel('Normalized Closing Price')
plt.show()