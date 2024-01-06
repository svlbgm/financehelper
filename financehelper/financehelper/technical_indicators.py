# financehelper/technical_indicators.py

# To Calculate Simple Moving Averages (SMA) and Relative Strength Index (RSI)
# integers given below are as usage examples, please read the docstrings for further information.

def calculate_sma(data, window=5):
    """
    Calculate Simple Moving Averages (SMA) for a given data set.

    Parameters:
    - data (list): List of dictionaries representing historical data.
    - window (int): The window size for the moving average calculation. Should be a positive integer.

    Returns:
    - list: List of SMA values, where each value corresponds to the SMA for a specific data point.
    """
    if type(window) is not int or window <= 0:
        raise ValueError("Window size should be a positive integer.")

    sma_values = []
    for i in range(len(data)):
        if i < window - 1:
            sma_values.append(None)  # Not enough data for the window
        else:
            # Extracting the close prices for the current window
            close_prices = [float(data[j]['Close']) for j in range(i - window + 1, i + 1)]
            # Calculating the Simple Moving Average
            sma = sum(close_prices) / window
            sma_values.append(sma)
    return sma_values


def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI) for a given data set.

    Parameters:
    - data (list): List of dictionaries representing historical data.
    - window (int): The window size for the RSI calculation. Should be a positive integer.

    Returns:
    - list: List of RSI values, where each value corresponds to the RSI for a specific data point.
    """
    if type(window) is not int or window <= 0:
        raise ValueError("Window size should be a positive integer.")

    rsi_values = []
    gains = losses = 0

    for i in range(1, len(data)):
        # Calculating the difference between consecutive days' closing prices
        close_diff = float(data[i]['Close']) - float(data[i - 1]['Close'])

        # Updating gains and losses based on the price difference
        if close_diff > 0:
            gains += close_diff
        elif close_diff < 0:
            losses -= close_diff

        if i >= window:
            # Calculating average gains and losses over the specified window
            avg_gain = gains / window
            avg_loss = losses / window

            # Calculating the Relative Strength (RS)
            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi = 100 - (100 / (1 + rs))
            rsi_values.append(rsi)

            # Updating the gains and losses for the next iteration
            gains = max(0, gains + close_diff)
            losses = max(0, losses - close_diff)

    return rsi_values

