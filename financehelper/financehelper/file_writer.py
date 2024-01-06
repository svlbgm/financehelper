# financehelper/file_writer.py

def write_to_csv(file_path, header, values):
    """
    Write data to a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.
    - header (list): The header for the CSV file.
    - values (list): The values to be written to the CSV file.

    Returns:
    None
    """
    # Opening the CSV file in write mode
    with open(file_path, 'w') as file:
        # Writing the header to the first line of the file
        file.write(','.join(header) + '\n')
        # Writing each value to a new line in the file(values are converted to strings before writing)
        for value in values:
            file.write(str(value) + '\n')

