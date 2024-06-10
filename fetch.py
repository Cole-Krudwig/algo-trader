import pandas as pd
import numpy as np
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