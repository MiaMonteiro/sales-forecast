import pandas as pd
import os

def dataloader(file_name, directory=None, **kwargs): #m
    """
    Loads a CSV file into a pandas Dataframe

    This function supports:
    - Absolute paths (e.g., `/home/user/data.csv`, `C:\\Users\\user\\data.csv`)
    - Relative paths (e.g., `data.csv`, `subfolder/data.csv`)

    Parameters:
    - file_name (str): Name of the CSV file (with the .csv extension)
    - directory (str, optional): Directory path where the file is located. Defaults to the current working directory
    - **kwargs: Additional arguments for pandas `read_csv()`

    Returns:
    - pd.DataFrame: Loaded Dataframe    

    Raises:
    - FileNotFoundError: If the file does not exist at the specified path
    - ValueError: If there is an error during the CSV loading process (e.g., malformed CSV)

    ##############

    Loads a CSV file into a pandas DataFrame.

    :param file_name str: 
    Name of the CSV file (with the .csv extension).

    :param directory str, optional: 
    Directory path where the file is located. Defaults to the current working directory.

    :param kwargs: 
    Additional arguments for pandas `read_csv()`.

    :return: 
    pd.DataFrame: Loaded DataFrame.

    :raises FileNotFoundError: 
    If the file does not exist at the specified path.

    :raises ValueError: 
    If there is an error during the CSV loading process (e.g., malformed CSV).
    
    """
    # If a directory is provided, join it with the file name
    if directory:
        file_path = os.path.join(directory, file_name)
    # If not, assume that it's in the current working directory
    else:
        file_path = file_name

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Load the CVS
    try:
        df = pd.read_csv(file_path, **kwargs)
        return df
    except Exception as e:
        raise ValueError(f'Error loading CSV:{e}')
    
df = dataloader('Different_stores_dataset.csv', '..\\OneDrive - FCT NOVA\\Ambiente de Trabalho\\baby')
print(df)

def remove_zero_neg_values(): #s
    """
    Removes rows where any of the specified columns contain zero or negative values
    """
    pass

def remove_duplicates(df): #m
    """
    Removes duplicated rows in the DataFrame.

    :param df pd.DataFrame: 
    The DataFrame from which duplicates will be removed.

    :return: 
    pd.DataFrame: A DataFrame with duplicated rows removed.
    """
    df = df.drop_duplicates()
    return df


def remove_missing_values(): #s
    """
    Remove rows where any of the specified columns contain missing values
    """
    pass

def remove_invalid_format(df, column_name, pattern): #m
    """
    Removes rows where the values in the specified column do not fully match the given format.

    :param df pd.DataFrame: 
    The DataFrame to check.

    :param column_name str: 
    The name of the column to validate.

    :param pattern str: 
    The regular expression pattern the values in the column must fully match.

    :return: 
    pd.DataFrame: A DataFrame with rows that don't fully match the format removed.
    """
    df = df[df[column_name].str.fullmatch(pattern, na=False)]
    return df


def check_invalid_dates(): #s
    """Removes entries with invalid date formats
    """

    pass

def main():
    pass

main()