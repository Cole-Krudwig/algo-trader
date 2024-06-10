# Algo Trading Backtester

## Author
Cole J. Krudwig

## Table of Contents
1. [Overview](#overview)
2. [Modules](#modules)
    - [Fetcher](#fetcher)
    - [Portfolio](#portfolio)
    - [Backtester](#backtester)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Fetching Data](#fetching-data)
    - [Managing Portfolio](#managing-portfolio)
    - [Running Backtests](#running-backtests)
5. [Example Strategy](#example-strategy)
6. [Contributing](#contributing)

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

fetcher = Fetcher('AAPL', '1h', 300)
data = fetcher.fetch()
```

### Managing Portfolio
Instantiate the Portfolio class with an initial capital amount. Use the update method to modify the portfolio's capital based on trading activity. Use the get_history method to retrieve the portfolio's capital history as a pandas DataFrame.

```python
from portfolio import Portfolio

portfolio = Portfolio(initial_capital=10000)
portfolio.update(date, price_diff, position)
history = portfolio.get_history()
```

### Running Backtests
```python
from backtester import Backtester
from strategy import simple_moving_average_strategy

backtester = Backtester(data)
backtester.set_strategy(simple_moving_average_strategy)
backtester.run()
results = backtester.results()
print(results)
```

## Example Strategy
The simple_moving_average_strategy function is an example strategy that uses a simple moving average crossover to generate buy/sell signals.

This strategy is intended to be illustrative of how strategies can interact with the different algo-trader modules and is not meant to be interpreted as a viable trading strategy or financial advice.

```python
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
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.
