import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


'''
This graph is a visual representation of a K-means clustering analysis on a set of stocks. 
The stocks are grouped into four clusters based on two features: their mean return and their standard deviation.
The mean return, represented on the y-axis, is a measure of the average performance of a stock. 
A higher mean return indicates that the stock has, on average, performed better over the time period considered.
The standard deviation, represented on the x-axis, is a measure of the volatility of a stock. 
A higher standard deviation indicates that the stock's returns have fluctuated more widely over the time period considered.
The four clusters represent groups of stocks that have similar characteristics in terms of these two features:

Low return, low volatility stocks (green): These stocks have lower average returns and lower volatility. 
    They are typically considered safer investments, but with lower potential for high returns.

Low return, high volatility stocks (red): These stocks have lower average returns but higher volatility. 
    They are generally considered riskier investments, and they have not necessarily provided high returns to compensate for their higher risk.

High return, low volatility stocks (blue): These stocks have higher average returns and lower volatility. 
        They are typically considered ideal investments, offering good returns with less risk.

High return, high volatility stocks (orange): These stocks have both higher average returns and higher volatility. 
    They have the potential for high returns, but they also carry a higher risk.

Each point on the graph represents a stock, and the color of the point indicates which cluster the stock belongs to. 

The ticker symbol for each stock is also displayed next to its corresponding point.
Please note that this is a simplified interpretation and the actual interpretation may vary depending 
on the specific characteristics of the stocks and the time period considered. Also, while this graph provides a 
useful visualization of the stocks' performance and volatility, it should not be the sole basis for investment decisions. 
Other factors such as the company's financial health, the state of the economy, and the specific risks associated with the 
company's industry should also be considered.
'''

# Load the data from the CSV file
data = pd.read_csv('all_data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Calculate the daily returns for each ticker
data['Return'] = data.groupby('Symbol')['Close'].pct_change()

# Calculate the mean daily return and standard deviation for each ticker
mean_returns = data.groupby('Symbol')['Return'].mean()
std_devs = data.groupby('Symbol')['Return'].std()

# Create a DataFrame with the mean returns and standard deviations
features = pd.DataFrame({'Mean Return': mean_returns, 'Standard Deviation': std_devs})

# Fit the KMeans model to the data
kmeans = KMeans(n_clusters=4, random_state=0).fit(features)

# Add the cluster labels to the features DataFrame
features['Cluster'] = kmeans.labels_

# Define the cluster descriptions
cluster_descriptions = {
    0: 'Low return, low volatility stocks',
    1: 'Low return, high volatility stocks',
    2: 'High return, low volatility stocks',
    3: 'High return, high volatility stocks'
}

# Create a scatter plot for each cluster
for cluster in features['Cluster'].unique():
    cluster_data = features[features['Cluster'] == cluster]
    plt.scatter(cluster_data['Standard Deviation'], cluster_data['Mean Return'], label=cluster_descriptions[cluster])
    
    # Add annotations for each point
    for i, txt in enumerate(cluster_data.index):
        plt.annotate(txt, (cluster_data['Standard Deviation'].iloc[i], cluster_data['Mean Return'].iloc[i]))

# Add labels and title
plt.xlabel('Standard Deviation')
plt.ylabel('Mean Return')
plt.title('K-Means Clustering of Stocks')

# Add a legend
plt.legend(title='Clusters', title_fontsize='13', loc='upper left')

# Show the plot
plt.show()