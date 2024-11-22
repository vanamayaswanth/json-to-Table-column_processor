
# JSON Column Processor

A Python library to process DataFrames containing nested JSON columns by flattening them into individual columns. This library is easy to use and designed with best practices, enabling developers to work efficiently with JSON data.

## Features

- Expand nested JSON data in DataFrame columns into separate columns.
- Handles complex, nested JSON structures.
- Provides a clean API for integration.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd json_column_processor
    ```

2. Install the library in editable mode:
    ```bash
    pip install -e .
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

```plaintext
json_column_processor/
├── json_column_processor/      # Main library package
│   ├── __init__.py             # Package initialization
│   ├── processor.py            # Core functionality
├── tests/                      # Unit tests for the library
│   ├── __init__.py
│   ├── test_processor.py
├── example/                    # Example usage files
│   ├── example_usage.py
├── LICENSE                     # License file (e.g., MIT)
├── README.md                   # Project documentation
├── setup.py                    # Package setup script
├── pyproject.toml              # Configuration for modern builds (optional)
├── .gitignore                  # Git ignore file
└── requirements.txt            # Dependencies
```

## Usage

1. Import the library:
    ```python
    from json_column_processor.processor import process_dataframe
    ```

2. Example usage:
    ```python
    import pandas as pd
    from json_column_processor.processor import process_dataframe

    # Example DataFrame
    data = {
        "Name": ["Alice", "Bob"],
        "Place": ["New York", "Paris"],
        "Dob": ["1990-01-01", "1985-05-12"],
        "Json": [
            '{"key1": "value1", "key2": "value2"}',
            '{"key1": "value3", "key2": "value4"}'
        ]
    }
    df = pd.DataFrame(data)

    # Process the DataFrame
    result = process_dataframe(df, "Json")
    print(result)
    ```

3. Run the example script:
    ```bash
    python example/example_usage.py
    ```

## Testing

1. Run unit tests:
    ```bash
    pytest tests/
    ```

## Troubleshooting

- If you encounter a `ModuleNotFoundError`, ensure the project is installed in editable mode and the correct Python environment is active.
- Verify the directory structure and ensure `__init__.py` files are present.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature-name'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
