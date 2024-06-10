"""
Simple Moving Average Trading Strategy
=====================================

Author: Cole J. Krudwig

Description:
------------
This file is a simple moving average trading strategy that is meant to illustrate how to use the backtesting, portfolio, and fetcher modules.
"""

import pandas as pd
import numpy as np
import sys
import os

# Define the base directory and pickle file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
print(BASE_DIR)

from fetch import Fetcher
from backtest import Backtester

def simple_moving_average_strategy(data):
    short_window = 40
    long_window = 100
    
    signals = pd.DataFrame(index=data.index)
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    if signals['short_mavg'].iloc[-1] > signals['long_mavg'].iloc[-1]:
        return 'buy'
    else:
        return 'sell'

# example ussage with Apple stock
fetcher = Fetcher('AAPL', '1h', 300)
data = fetcher.fetch()

backtester = Backtester(data)
backtester.set_strategy(simple_moving_average_strategy)
backtester.run()
results = backtester.results()

print(results)