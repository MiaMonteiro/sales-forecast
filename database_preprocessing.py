import pandas as pd
from typing import List

def dataloader(): #m
    """it loads
    """
    pass

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

def remove_duplicates(): #m
    """
    Removes duplicated rows in the Dataframe
    """
    pass

def remove_missing_values(): #S
    """
    Remove rows where any of the specified columns contain missing values
    """
    pass

def check_variable_format(): #M
    """
    It checks if codes are in the correct format for their specific type
    """
    pass

def check_invalid_dates(): #S
    """Removes entries with invalid date formats
    """

    pass

def main():
    pass

main()