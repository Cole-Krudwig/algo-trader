import yfinance as yf
import pandas as pd
import numpy as np
from portfolio import Portfolio
from fetch import Fetcher

class Backtester:
    def __init__(self, data, initial_capital=10000):
        self.data = data
        self.portfolio = Portfolio(initial_capital)
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def run(self):
        if self.strategy is None:
            raise ValueError("Strategy not set.")
        
        self.portfolio.reset()
        positions = 0
        
        for i in range(1, len(self.data)):
            date = self.data.index[i]
            price = self.data['Close'].iloc[i]
            prev_price = self.data['Close'].iloc[i-1]
            signal = self.strategy(self.data.iloc[:i+1])

            if signal == 'buy' and positions == 0:
                positions = self.portfolio.capital // price  # Assuming integer shares
            elif signal == 'sell' and positions > 0:
                price_diff = price - prev_price
                self.portfolio.update(date, price_diff, positions)
                positions = 0

        if positions > 0:
            final_price = self.data['Close'].iloc[-1]
            self.portfolio.update(self.data.index[-1], final_price - prev_price, positions)
    
    def results(self):
        return self.portfolio.get_history()
    

fetcher = Fetcher('aapl', '1h', 300)
data = fetcher.fetch()
print(data)


