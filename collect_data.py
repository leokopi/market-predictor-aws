# file with a purpose of fetching data for analysis from APIs and basic data handling methods

import yfinance as yf # fetch financial data from yahoo finace api
import pandas as pd #data manipulation and analysis library
from datetime import datetime # for working with datas and times
from config import S3_BUCKET_NAME, S3_RAW_DATA_PREFIX, TICKERS, DATA_PERIOD

print('Fetching Bitcoin data...')
btc = yf.Ticker("BTC-USD")
btc_data = btc.history(period="1mo")
print(btc_data.head())
print(f"\nShape of data: {btc_data.shape}")

# Save the data to a CSV file
# This creates a local backup and lets us inspect the data structure
filename = f"bitcoin_data_{datetime.now().strftime('%Y%m%d')}.csv"
btc_data.to_csv(filename)
print(f"\nData saved to {filename}")