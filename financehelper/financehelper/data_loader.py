# This code definition takes and returns the data of the selected file path

# Function to load historical data from a CSV file
def load_data(file_path):
    # Initializing an empty list to store the data
    data = []
    # Opening the CSV file in read mode
    with open(file_path, 'r') as file:
        # Reading all lines from the file
        lines = file.readlines()
        # Extracting the header (column names) from the first line
        header = lines[0].strip().split(',')
        # Iterating through the remaining lines
        for line in lines[1:]:
            # Splitting each line into values using ',' as the delimiter
            values = line.strip().split(',')
            #  Creating a dictionary for each data point with headers (column names) as keys
            # and corresponding values for each column
            data_point = {header[i]: values[i] for i in range(len(header))}
            # Appending the data point dictionary to the data list that has been initialized before
            data.append(data_point)
    # Returning the list of dictionaries as the loaded data
    return data
