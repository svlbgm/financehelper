# FinanceHelper

FinanceHelper is a Python package that provides tools for financial data analysis. 
It includes functions for loading historical data, calculating technical indicators, and writing data to CSV files.

## Installation

You can install FinanceHelper using pip:

```bash
pip install financehelper

```

# * USAGE : *

from financehelper.data_loader import load_data

# Load historical data from a CSV file
file_path = 'path/to/your/data.csv'

historical_data = load_data(file_path)

# Calculating Simple Moving Averages (SMA)
from financehelper.technical_indicators import calculate_sma

## Calculate SMA for a 5-day window
sma_values = calculate_sma(historical_data, window=5)

from financehelper.technical_indicators import calculate_rsi

## Calculate RSI for a 14-day window
rsi_values = calculate_rsi(historical_data, window=14)

# Writing Results to CSV
from financehelper.file_writer import write_to_csv

# Write SMA values to a CSV file
write_to_csv('sma_results.csv', ['SMA'], sma_values)

# Write RSI values to a CSV file
write_to_csv('rsi_results.csv', ['RSI'], rsi_values)

# EXAMPLE USAGE:
 ! A main.py is also included in the package as an example for better understanding,
 it is recommended for you to check before implementing to your own project.
# Import necessary functions
from financehelper.data_loader import load_data
from financehelper.technical_indicators import calculate_sma, calculate_rsi
from financehelper.file_writer import write_to_csv

# Load historical data
historical_data = load_data('path/to/your/data.csv')

# Calculate SMA and RSI
sma_values = calculate_sma(historical_data, window=5)
rsi_values = calculate_rsi(historical_data, window=14)

# Write results to CSV
write_to_csv('sma_results.csv', ['SMA'], sma_values)
write_to_csv('rsi_results.csv', ['RSI'], rsi_values)

# Note:

# Make sure to replace the placeholders such as `'path/to/your/data.csv'` with the actual paths and filenames relevant to your project. Additionally, customize the examples and usage scenarios to match the functionality and features of your package.

