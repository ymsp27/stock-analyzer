import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetching the data - API call
ticker = "AAPL"
stock = yf.Ticker(ticker)
data = stock.history(period="1y")

# Analysing - Daily Returns
data['Daily Return'] = data['Close'].pct_change() * 100
avg_return = data['Daily Return'].mean()
print(f"Average daily return for {ticker}: {avg_return: .2f}%")

# Plot prices and returns
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(data.index, data['Close'], label='Close Price')
ax1.set_title(f"{ticker} Stock Price")
ax1.legend()

ax2.plot(data.index, data['Daily Return'], color='green', alpha=0.7)
ax2.set_title("Daily Returns (%)")
ax2.axhline(y=0, color='black', linestyle="--")

plt.tight_layout()
plt.show()

# Saving the output into CSV format
data.to_csv('aapl_data.csv')
print("Data saved to appl_data.csv")
