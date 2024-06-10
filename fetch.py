"""
Fetcher Module
==============

Author: Cole J. Krudwig

Description:
------------
This module defines a Fetcher class that uses the yfinance library to fetch historical 
stock data for a specified asset, interval, and period. The fetched data includes open, 
high, low, close, adjusted close prices, and volume.

Usage:
------
Instantiate the Fetcher class with the asset symbol, data interval, and number of days 
for which data is required. Use the fetch method to retrieve the data as a pandas DataFrame.

Example:
--------
fetcher = Fetcher('AAPL', '1h', 30)
data = fetcher.fetch()
"""

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

class Fetcher:
    def __init__(self, asset, interval, days):
        self.asset = asset
        self.interval = interval
        self.days = days
        self.end_date = datetime.today()
        self.start_date = self.end_date - timedelta(days=self.days)

    def fetch(self):
        df = pd.DataFrame()

        fetched_data = yf.download(self.asset, start=self.start_date, end=self.end_date, interval='1h')
        
        if df.empty:
            df = fetched_data
        else:
            df = pd.merge(df, fetched_data, left_index=True, right_index=True, how='inner')

        return df