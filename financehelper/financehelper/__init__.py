# financehelper/__init__.py
from .data_loader import load_data
from .technical_indicators import calculate_sma, calculate_rsi
from .file_writer import write_to_csv

# If the codes for importation is written as below ,in another python file while this package is installed:
# from financehelper import load_data, calculate_sma, calculate_rsi, write_to_csv
# a direct access to these functions will be granted.

# package version info:
__version__ = '0.1.0'
