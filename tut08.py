# Importing necessary libraries
import pandas as pd

# Load the dataset
file_path = 'infy_stock.csv'  # Provide the correct file path here
df = pd.read_csv(file_path)

# Display the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))
print(df.shape)

# Checking for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Handling missing values (if any) by dropping them
df = df.dropna()
print("\nAfter handling missing values, new dataset shape:")
print(df.shape)

import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Date' to datetime format for plotting
df['Date'] = pd.to_datetime(df['Date'])

# Plot closing price over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Close')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()
!pip install mplfinance

# Import the necessary module
import mplfinance as mpf

# Set 'Date' as the index for the candlestick chart
df.set_index('Date', inplace=True)

# Plot candlestick chart for stock prices
mpf.plot(df, type='candle', volume=True, style='yahoo', title="Candlestick Chart of Stock Prices")

# Calculate the daily return percentage
df['Daily Return %'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Display the first few rows with the new column
print("\nDaily Return Percentage:")
print(df[['Open', 'Close', 'Daily Return %']].head(10))

# Calculate average and median of daily returns
average_return = df['Daily Return %'].mean()
median_return = df['Daily Return %'].median()

# Calculate standard deviation of the closing prices
std_dev_close = df['Close'].std()

print(f"\nAverage Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Closing Prices: {std_dev_close:.2f}")

# Calculate 50-day and 200-day moving averages
df['50-day MA'] = df['Close'].rolling(window=50).mean()
df['200-day MA'] = df['Close'].rolling(window=200).mean()

# Plotting the closing price along with 50-day and 200-day moving averages
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Closing Price')
plt.plot(df.index, df['50-day MA'], label='50-Day Moving Average', color='orange')
plt.plot(df.index, df['200-day MA'], label='200-Day Moving Average', color='red')
plt.title('Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# The 'Date' column is already the index, so no need to set it again
# Calculate the 30-day rolling standard deviation (volatility)
#calculation of how much a stock's price fluctuates over a recent 30-day period, with the result being updated each day.
df['30-day Volatility'] = df['Close'].rolling(window=30).std()

# Plotting the volatility over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['30-day Volatility'], label='30-Day Rolling Volatility', color='red')
plt.title('Stock Volatility Over Time (30-Day Rolling Std Dev)')
plt.xlabel('Date')
plt.ylabel('Volatility (Standard Deviation)')
plt.legend()
plt.show()

# Identify bullish and bearish trends
df['Trend'] = 'Neutral'
df.loc[df['50-day MA'] > df['200-day MA'], 'Trend'] = 'Bullish'  # Bullish trend
df.loc[df['50-day MA'] < df['200-day MA'], 'Trend'] = 'Bearish'  # Bearish trend

# Print first few rows to check trend identification
print("\nTrend Identification based on Moving Averages:")#general direction of the stock's price movement.
print(df[['50-day MA', '200-day MA', 'Trend']].head(10))

# Highlight bullish and bearish trends
plt.fill_between(df.index, df['Close'], where=(df['50-day MA'] > df['200-day MA']), color='blue', alpha=0.3, label='Bullish Trend')
plt.fill_between(df.index, df['Close'], where=(df['50-day MA'] < df['200-day MA']), color='yellow', alpha=0.3, label='Bearish Trend')

# Title and labels
plt.title('Stock Price with Bullish and Bearish Trends (50-day vs. 200-day MA)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()