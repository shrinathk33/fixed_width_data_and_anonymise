# CSV Anonymization Script

## Overview

This script is designed to anonymize sensitive data in a large CSV file by replacing values in specific columns (`first_name`, `last_name`, and `address`) with randomly generated data. 
## Features

- **Chunked Processing**: Processes the CSV file in chunks to handle large datasets without exhausting system memory.
- **Distributed computing**: This code is rewritten in pyspark to demonstrate disributed computing.
## Requirements

- Python 3.x
- Pandas
- Faker
- Pyspark

## Installation

To install the necessary Python packages, run:

```bash
pip install pandas faker pyspark
```