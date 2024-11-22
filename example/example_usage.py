import pandas as pd
from json_column_processor.processor import *

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
result = process_dataframe(df, json_column="Json")
print(result)
