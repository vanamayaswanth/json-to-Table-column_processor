import pandas as pd
import json

def flatten_json(nested_json, parent_key='', sep='_'):
    """
    Recursively flattens a nested JSON object into a single-level dictionary.

    Args:
        nested_json (dict): The nested JSON object.
        parent_key (str): The base key string for the flattened keys.
        sep (str): Separator used for nested keys.

    Returns:
        dict: A flattened dictionary.
    """
    items = []
    if isinstance(nested_json, dict):
        for k, v in nested_json.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_json(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    items.extend(flatten_json({f"{new_key}_{i}": item}, sep=sep).items())
            else:
                items.append((new_key, v))
    return dict(items)

def process_dataframe(df, json_column, sep='_'):
    """
    Processes a DataFrame with a JSON column by flattening the JSON into new columns.

    Args:
        df (pd.DataFrame): Original DataFrame.
        json_column (str): Name of the column containing JSON data.
        sep (str): Separator used for flattened keys.

    Returns:
        pd.DataFrame: Concatenated DataFrame with original and flattened JSON columns.
    """
    original_df = df.copy()

    try:
        manipulated_df = df[[json_column]].copy()
        manipulated_df[json_column] = manipulated_df[json_column].apply(
            lambda x: flatten_json(json.loads(x), sep=sep) if isinstance(x, str) else flatten_json(x, sep=sep)
        )
        flattened_df = pd.json_normalize(manipulated_df[json_column])
    except Exception as e:
        raise ValueError(f"Error processing JSON column: {e}")

    result_df = pd.concat([original_df, flattened_df], axis=1)
    result_df = result_df.drop(columns=[json_column], errors='ignore')

    return result_df
