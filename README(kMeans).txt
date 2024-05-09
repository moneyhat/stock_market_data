K-Means Clustering for Stock Analysis

This Python script performs a K-means clustering analysis on a set of stocks based on their mean return and standard deviation. It then visualizes the results using a scatter plot, grouping the stocks into four clusters with different characteristics in terms of performance and volatility. The script uses pandas for data manipulation and matplotlib for plotting.

Requirements
Python 3
pandas
matplotlib
sklearn

Usage
Install the required libraries if not already installed:

pip install pandas matplotlib sklearn
Download historical stock price data for multiple tickers and save it as 'all_data.csv'. This file should have columns like 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume'.
Run the script:

python kmeans.py

The script will:
Load the data from 'all_data.csv'.
Convert the 'Date' column to datetime format and set it as the index.
Calculate daily returns for each ticker.
Calculate the mean daily return and standard deviation for each ticker.
Create a DataFrame containing the mean returns and standard deviations.
Perform K-means clustering on the data using four clusters.
Add cluster labels to the features DataFrame.
Create a scatter plot for each cluster, displaying the stocks' mean return vs. standard deviation, and color-coding them based on their cluster membership.
Annotate each point with the corresponding ticker symbol.
Add labels, title, and legend to the plot.
Display the final plot showing the K-means clustering results.

Output
After running the script, a scatter plot will be displayed showing the clustering results based on mean return and standard deviation. Four clusters are present in the graph, each representing a different combination of performance and volatility characteristics. The color of each point indicates which cluster the stock belongs to, and the ticker symbol is displayed next to its corresponding point.

Please note that this is a simplified interpretation, and actual investment decisions should consider other factors such as the company's financial health, economic conditions, and industry-specific risks.