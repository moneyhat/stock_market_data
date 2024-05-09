import pandas as pd
import matplotlib.pyplot as plt

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

# Create the categories
low_risk_high_reward = (mean_returns > mean_returns.median()) & (std_devs < std_devs.median())
high_risk_high_reward = (mean_returns > mean_returns.median()) & (std_devs > std_devs.median())
low_risk_low_reward = (mean_returns < mean_returns.median()) & (std_devs < std_devs.median())
high_risk_low_reward = (mean_returns < mean_returns.median()) & (std_devs > std_devs.median())

# Create a scatter plot for each category
plt.scatter(std_devs[low_risk_high_reward], mean_returns[low_risk_high_reward], color='green', label='Low Risk, High Reward')
plt.scatter(std_devs[high_risk_high_reward], mean_returns[high_risk_high_reward], color='red', label='High Risk, High Reward')
plt.scatter(std_devs[low_risk_low_reward], mean_returns[low_risk_low_reward], color='blue', label='Low Risk, Low Reward')
plt.scatter(std_devs[high_risk_low_reward], mean_returns[high_risk_low_reward], color='orange', label='High Risk, Low Reward')

# Add annotations for each point
for i, txt in enumerate(std_devs.index):
    plt.annotate(txt, (std_devs[i], mean_returns[i]))

plt.xlabel('Standard Deviation')
plt.ylabel('Mean Return')
plt.title('Mean Return vs. Standard Deviation for Each Ticker')
plt.legend()
plt.show()