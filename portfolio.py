"""
Portfolio Module
================

Author: Cole J. Krudwig

Description:
------------
This module defines a Portfolio class that manages the capital allocation and tracks 
the capital history over time during the execution of a trading strategy. It allows 
resetting of the portfolio and updating the capital based on trading actions.

Usage:
------
Instantiate the Portfolio class with an initial capital amount. Use the update method 
to modify the portfolio's capital based on trading activity. Use the get_history method 
to retrieve the portfolio's capital history as a pandas DataFrame.

Example:
--------
portfolio = Portfolio(initial_capital=10000)
portfolio.update(date, price_diff, position)
history = portfolio.get_history()
"""

import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital
        self.positions = 0
        self.capital = initial_capital
        self.capital_history = []

    def reset(self):
        self.capital = self.initial_capital
        self.capital_history = []

    def update(self, date, price_diff, position):
        self.capital += price_diff * position
        self.capital_history.append((date, self.capital))

    def get_history(self):
        return pd.DataFrame(self.capital_history, columns=['Date', 'Capital'])
    
