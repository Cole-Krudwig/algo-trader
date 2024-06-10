# Algo Trading Backtester

## Author
Cole J. Krudwig

## Date
06/10/2024

## Overview
The Algo Trading Backtester is a Python-based project that allows users to define and backtest trading strategies. The project includes modules for fetching historical market data, managing a trading portfolio, and running backtests on specified strategies.

## Modules
### Fetcher
The `Fetcher` module uses the yfinance library to fetch historical stock data for a specified asset, interval, and period. The data includes open, high, low, close, adjusted close prices, and volume.

### Portfolio
The `Portfolio` module manages the capital allocation and tracks the capital history over time during the execution of a trading strategy. It allows resetting the portfolio and updating the capital based on trading actions.

### Backtester
The `Backtester` module simulates the execution of a trading strategy over historical market data. It interacts with the `Portfolio` class to track the capital over time and generate results based on the strategy's performance.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/algo-trading-backtester.git
    ```
2. Change to the project directory:
    ```bash
    cd algo-trading-backtester
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Fetching Data
Instantiate the `Fetcher` class with the asset symbol, data interval, and number of days for which data is required. Use the `fetch` method to retrieve the data as a pandas DataFrame.

```python
from fetcher import Fetcher

fetcher = Fetcher('AAPL', '1h', 30)
data = fetcher.fetch()
