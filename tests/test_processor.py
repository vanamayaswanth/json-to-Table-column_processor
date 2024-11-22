import pytest
import pandas as pd
from json_column_processor.processor import process_dataframe

def test_process_dataframe():
    data = {
        "Name": ["John", "Jane"],
        "Place": ["New York", "Los Angeles"],
        "Dob": ["1990-01-01", "1995-05-15"],
        "Json": [
            '{"info": {"city": "Manhattan", "zipcode": "10001"}, "active": true, "preferences": {"color": "blue", "food": "pizza"}}',
            '{"info": {"city": "Hollywood", "zipcode": "90001"}, "active": false, "preferences": {"color": "green", "food": "sushi"}}'
        ]
    }
    df = pd.DataFrame(data)
    json_column = "Json"
    result = process_dataframe(df, json_column=json_column)

    assert "info_city" in result.columns
    assert "active" in result.columns
    assert result.loc[0, "info_city"] == "Manhattan"
    assert result.loc[1, "preferences_food"] == "sushi"
