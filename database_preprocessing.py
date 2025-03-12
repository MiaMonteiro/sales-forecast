import pandas as pd
import os
from typing import List

def dataloader(file_name, directory=None, **kwargs): #m
    """
    Loads a CSV file into a pandas DataFrame.

    
    This function supports:
    - Absolute paths (e.g., `/home/user/data.csv`, `C:\\Users\\user\\data.csv`)
    - Relative paths (e.g., `data.csv`, `subfolder/data.csv`)

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
    

def remove_zero_neg_values(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame: #S
    """
    Removes rows where any of the specified columns contain zero or negative values.

    :param df pd.DataFrame: 
    Pandas Dataframe containing the data.

    :param columns List[str]: 
    List of column names (str) to check for negative or zero values.

    :return: 
    pd.DataFrame without the zero or negative values.

    :raises ValueError: 
    If any of the specified columns do not exist in the dataframe
    """
    # Find missing columns
    missing_columns = [column for column in columns if column not in df.columns]

    # Raise exception if columns are missing
    if missing_columns:
        raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

    # create a dataframe where true meand df[columns] > 0. Checks if all values are True in a row, if not, the row is removed.
    mask = (df[columns] > 0).all(axis=1)

    return df[mask]


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


def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame: #S
    """
    Remove rows where there is atleast one missing value. Prints a report giving the number of rows removed due to missing values.

    :param df pd.DataFrame:
    A pandas DataFrame containing the data

    :return:
    pd.DataFrame without the rows containing missing values
    """
    # get the initial number of rows
    initial_rows = len(df)

    # remove rows with missing values
    df.dropna(inplace=True)

    # get number of rows after removing missing values
    removed_rows = initial_rows - len(df)
    
    # inform user
    print(f"Removed {removed_rows} rows due to missing values.")

    return df


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

    :raises ValueError: 
    If the specified column does not exist in the DataFrame.

    :raises TypeError: 
    If pattern is not a string.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    
    # Ensure pattern is a string to use pd.str.fullmatch
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string.")

    # Filters rows where the values in the specific column don't fully match to the pattern given
    df = df[df[column_name].str.fullmatch(pattern, na=False)]
    return df


def check_invalid_dates(): #s
    """Removes entries with invalid date formats
    """

    pass

def main():
    pass

main()