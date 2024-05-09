Normalized Closing Price Plot for Top Performing Stocks

This Python script loads historical stock price data from a CSV file, normalizes the closing prices by their initial value, identifies the top 8 performing stocks (excluding '^GSPC'), and plots their normalized closing prices over time along with '^GSPC'. The script uses pandas for data manipulation and matplotlib for plotting.

Requirements
Python 3
pandas
matplotlib

Usage
1.Install the required libraries if not already installed:
Shell Script
pip install pandas matplotlib
Download historical stock price data for multiple tickers and save it as 'all_data.csv'. This file should have columns like 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume'.

2.Run the script:

python normalized_prices.py


The script will:
1.Load the data from 'all_data.csv'.
2. Convert the 'Date' column to datetime format and set it as the index.
3.Normalize the closing prices by their initial price.
4.Get the final normalized closing price for each ticker.
5.Select the top 8 performing stocks (excluding '^GSPC').
6.Add '^GSPC' to the list of stocks to plot.
7.Plot the normalized closing prices of the selected stocks over time.
8.Display the plot with a legend, title, and labels for x-axis and y-axis.

Output
After running the script, a line plot will be displayed showing the normalized closing prices of the top 8 performing stocks and '^GSPC' over time. The plot will have a title, 'Normalized Closing Prices Over Time for Top 8 Performing Stocks and ^GSPC', and labels for the x-axis ('Date') and y-axis ('Normalized Closing Price'). Each line in the plot represents a different stock, and the line width for '^GSPC' is thicker than the others for better visual differentiation.