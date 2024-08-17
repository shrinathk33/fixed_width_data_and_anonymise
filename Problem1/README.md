# Fixed-Width File Parser

This project contains a Python script to generate a fixed-width file (`input.txt`) with 1000 rows based on a given specification. It also includes a parser to convert this fixed-width file into a delimited CSV file.

## Project Structure

```
.
├── Dockerfile              # Dockerfile to containerize the application
├── input.txt               # Generated fixed-width file with 1000 rows
├── problem1.py             # Main script to parse the fixed-width file and generate CSV
├── requirements.txt        # Python dependencies (if any)
├── spec.json               # Specification file for the fixed-width format
├── output.csv              # Generated CSV file after parsing (output)
└── README.md               # This file
```

## Spec File

The spec file (`spec.json`) defines the fixed-width file format:

```json
{
    "ColumnNames": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10"
    ],
    "Offsets": [
        "5",
        "12",
        "3",
        "2",
        "13",
        "7",
        "10",
        "13",
        "20",
        "13"
    ],
    "FixedWidthEncoding": "windows-1252",
    "IncludeHeader": "True",
    "DelimitedEncoding": "utf-8"
}
```

To parse the generated `input.txt` file and convert it into a CSV file:

1. Use the provided `main.py` script:
   ```bash
   python problem1.py
   ```
2. The output CSV file will be saved as `output.csv`.

## Docker Container

You can run the entire process inside a Docker container:

### Building the Docker Image

```bash
docker build -t fixed-width-parser .
```

### Running the Docker Container

```bash
docker run -v $(pwd):/app fixed-width-parser
```

This will automatically generate the `input.txt` file and convert it to a CSV file inside the container.

## Dependencies

- Python 3.x
- No external dependencies are required, but the standard library is used for file handling and CSV creation.
