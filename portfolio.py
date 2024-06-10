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
    
