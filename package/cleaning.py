from myDataLib.io import import_data
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

def handle_missing_values(df, strategy='mean', columns=None, fill_value=None):
    """
    Handles missing values in a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        strategy (str): 'mean', 'median', 'mode', 'constant', or 'drop'.
        columns (list, optional): List of columns to apply missing value handling to. 
          If None (default), all columns with missing values will be targeted.
        fill_value (any, optional): If strategy is 'constant', this is the value to use.

    Returns:
        pd.DataFrame: A DataFrame with missing values handled.
    """
    if columns is None:
        columns = df.columns[df.isnull().any()].tolist() # Apply to all columns if none specified.
    if not columns: #if empty list or None
        return df

    if strategy == 'drop':
      return df.dropna(subset = columns) #drop rows with nan in selected columns.
    elif strategy == 'constant':
      if fill_value is None:
        raise ValueError("Must provide a fill_value if strategy is 'constant'.")
      df[columns] = df[columns].fillna(fill_value)
    elif strategy in ['mean', 'median', 'mode']:
      imputer = SimpleImputer(strategy=strategy)
      df[columns] = imputer.fit_transform(df[columns])
    else:
      raise ValueError("Invalid strategy. Choose 'mean', 'median', 'mode', 'constant', or 'drop'.")
    return df

def remove_outliers_iqr(df, column, factor=1.5):
    """
    Removes outliers from a DataFrame column using the IQR method.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column to check for outliers.
        factor (float): The IQR multiplier to define upper and lower bounds.

    Returns:
        pd.DataFrame: A DataFrame with outliers removed from the specified column.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

def convert_column_type(df, column, dtype):
    """
    Converts a DataFrame column to a specific data type.
    Args:
      df (pd.DataFrame): The input DataFrame
      column (str) : The column to be changed.
      dtype (type): The type to convert to such as int, float, datetime
    Returns:
      pd.DataFrame: The updated DataFrame with the specified column type converted.
    """
    try:
        df[column] = df[column].astype(dtype)
    except Exception as e:
      print(f"Error converting column {column} to type {dtype}: {e}")
    return df

def normalize_data(df, columns, method='standard'):
    """
    Normalizes specified columns in a DataFrame using standard scaling or min-max scaling.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of columns to normalize.
        method (str): 'standard' for standard scaling or 'minmax' for min-max scaling.

    Returns:
        pd.DataFrame: The DataFrame with normalized columns.
    """
    if not columns:
      return df # Do nothing if no columns provided.

    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Invalid normalization method. Choose 'standard' or 'minmax'.")

    df[columns] = scaler.fit_transform(df[columns])
    return df

def remove_duplicates(df, subset=None, keep='first'):
    """
    Removes duplicate rows from a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        subset (list, optional): List of column names to consider for duplicates. If None, all columns are used.
        keep (str, optional): 'first', 'last', or False, determines which duplicates to keep.

    Returns:
        pd.DataFrame: A DataFrame with duplicate rows removed.
    """
    df = df.drop_duplicates(subset=subset, keep=keep)
    return df

def clean_text_column(df, column, lower=True, remove_space=True, remove_special=True):
    """Cleans a text column by converting to lowercase and/or removing spaces or special characters."""
    if lower:
        df[column] = df[column].str.lower()
    if remove_space:
      df[column] = df[column].str.strip()
    if remove_special: #Removes special chars, keeps letter and numbers.
        df[column] = df[column].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    return df

def clean_data(filepath, strategy='mean', outlier_cols=None, outlier_factor=1.5,
               normalize_cols=None, normalize_method='standard',
               convert_type = None, dup_subset = None, dup_keep='first',
               text_cols=None,text_lower=True, text_space=True, text_special=True):
    """
    Imports data and applies cleaning steps.

    Args:
        filepath (str): Path to the data file.
        strategy (str): Missing value handling strategy ('mean', 'median', 'mode', 'constant', 'drop').
        outlier_cols (list): Columns to remove outliers from.
        outlier_factor (float): IQR multiplier for outlier removal.
        normalize_cols (list): Columns to normalize.
        normalize_method (str): Normalization method ('standard', 'minmax').
        convert_type (dict) : A dictionary of column names to type {col_name:type}.
        dup_subset (list) : A list of column to consider duplicates, if none, all columns are considered.
        dup_keep (str): 'first', 'last', or False, determines which duplicates to keep.
        text_cols (list) : A list of columns to clean with text options.
        text_lower (bool): if True, all text will be lower case.
        text_space (bool) : if True, all space at the end will be removed.
        text_special (bool): If True, any special characters will be removed.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    df = import_data(filepath)
    if df is None:
      return None

    df = handle_missing_values(df, strategy)

    if outlier_cols:
      for col in outlier_cols:
        df = remove_outliers_iqr(df, col, outlier_factor)

    if normalize_cols:
        df = normalize_data(df, normalize_cols, normalize_method)

    if convert_type:
      for col, type in convert_type.items():
          df = convert_column_type(df,col,type)

    df = remove_duplicates(df, subset=dup_subset, keep=dup_keep)

    if text_cols:
      for col in text_cols:
        df = clean_text_column(df, col, lower=text_lower, remove_space=text_space, remove_special=text_special)

    return df