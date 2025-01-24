import pandas as pd
import os
import json

def import_data(filepath, file_type=None):
    """
    Imports data from various file formats into a pandas DataFrame.

    Args:
        filepath: Path to the data file.
        file_type: (Optional) Explicitly specify the file type ('csv', 'json', 'parquet', 'excel').
                   If None, it will be inferred from the file extension.

    Returns:
        A pandas DataFrame containing the imported data, or None if an error occurs.
        Prints an informative error message if the file is not found or the format is unsupported.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return None

    if file_type is None:
        file_type = filepath.split('.')[-1].lower()  # Infer from extension

    try:
        if file_type == 'csv':
            df = pd.read_csv(filepath)
        elif file_type == 'json':
            df = pd.read_json(filepath)
        elif file_type == 'parquet':
            df = pd.read_parquet(filepath)
        elif file_type in ['xls', 'xlsx']:
             df = pd.read_excel(filepath)
        else:
            print(f"Error: Unsupported file type '{file_type}'. Supported types are 'csv', 'json', 'parquet', and 'xls/xlsx'.")
            return None
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filepath}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse the file '{filepath}'. Check the file format and ensure it's valid.")
        return None
    except Exception as e:  # Catch other potential errors during import
        print(f"An unexpected error occurred while importing '{filepath}': {e}")
        return None


def export_data(df, filepath, file_type='csv', index=False, **kwargs):
    """
    Exports a pandas DataFrame to various file formats.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        filepath (str): The path to save the file.
        file_type (str, optional): The file format ('csv', 'json', 'parquet', 'excel'). Default is 'csv'.
        index (bool, optional): Whether to write the DataFrame index to the output file. Defaults to False.
        **kwargs: Additional keyword arguments for specific file formats.
            For JSON export use `orient='records'` to get records (row-wise) or 'index' to get column oriented output.
            For excel export use `sheet_name`.

    Returns:
        bool: True if export was successful, False otherwise.
    """
    try:
        if file_type == 'csv':
            df.to_csv(filepath, index=index, **kwargs)
        elif file_type == 'json':
          if 'orient' not in kwargs:
             kwargs['orient'] = 'records' # default to record output for json.
          df.to_json(filepath, index=index, **kwargs)
        elif file_type == 'parquet':
            df.to_parquet(filepath, index=index, **kwargs)
        elif file_type in ['xls','xlsx']:
             if 'sheet_name' not in kwargs:
                kwargs['sheet_name'] = 'Sheet1'
             df.to_excel(filepath, index=index, **kwargs)
        else:
             print(f"Error: Unsupported file type '{file_type}'. Supported types are 'csv', 'json', 'parquet', and 'xls/xlsx'.")
             return False
        return True
    except Exception as e:
        print(f"Error exporting data to '{filepath}': {e}")
        return False