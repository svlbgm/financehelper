# main_script.py

# This part of the script ( the python file) actually represents your own project that you are working on,
# and it does solely depend on making a better understanding while demonstrate the functionality of the package

# DISCLAIMER!
# When you are writing your OWN main script, these packages are going to be used on
# YOU MUST ensure that the directory containing "financehelper" is in your Python path
# or in the same directory as your main script.

# Assuming the main script is in a subdirectory of "financehelper"
# Both of the following importing options can be used :


from ..financehelper.data_loader import load_data
from ..financehelper.technical_indicators import calculate_sma, calculate_rsi
from ..financehelper.file_writer import write_to_csv


from .data_loader import load_data
from .technical_indicators import calculate_sma, calculate_rsi
from .file_writer import write_to_csv


# Specifying the file path
csv_file_path = 'orcl.csv'

# Loading data from the CSV file
historical_data = load_data(csv_file_path)

# Calculating SMA and RSI
sma_values = calculate_sma(historical_data)
rsi_values = calculate_rsi(historical_data)

# Specifying the file paths for SMA and RSI
sma_file_path = 'orcl-sma.csv'
rsi_file_path = 'orcl-rsi.csv'

# Writing SMA and RSI to files
write_to_csv(sma_file_path, ['SMA'], sma_values)
write_to_csv(rsi_file_path, ['RSI'], rsi_values)
