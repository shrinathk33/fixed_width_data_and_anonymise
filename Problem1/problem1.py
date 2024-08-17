import json
import csv
import random

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.csv'
SPEC_FILE = 'spec.json'

def pad_or_truncate(value, length):
    if len(value) > length:
        return value[:length]
    return value.ljust(length)

def generate_fixed_width_file(output_file, data, column_names, offsets, include_header=True, encoding="windows-1252"):
    with open(output_file, 'w', encoding=encoding) as f:
        if include_header:
            header = ''.join([pad_or_truncate(col, length) for col, length in zip(column_names, offsets)])
            f.write(header + '\n')

        for row in data:
            line = ''.join([pad_or_truncate(str(value), length) for value, length in zip(row, offsets)])
            f.write(line + '\n')


# Function to generate random data for the fields
def generate_random_data():
    return [
        f"{random.randint(10000, 99999)}",                       # f1
        ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=12)),  # f2
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3)),   # f3
        f"{random.randint(10, 99)}",                           # f4
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ', k=13)),  # f5
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=7)),   # f6
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=10)),  # f7
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=13)),  # f8
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ', k=20)),  # f9
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ', k=13))   # f10
    ]



def load_spec(spec_file):
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    return spec

# Generate 10000 rows of data
# column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
# offsets = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]

spec = load_spec(SPEC_FILE)
column_names = spec["ColumnNames"]
offsets = list(map(int, spec["Offsets"]))

data = [generate_random_data() for _ in range(10000)]
generate_fixed_width_file(INPUT_FILE, data, column_names, offsets)


def parse_fixed_width(file_path, spec):
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers
    encoding = spec["FixedWidthEncoding"]
    
    parsed_data = []
    
    with open(file_path, 'r', encoding=encoding) as f:
        if spec["IncludeHeader"] == "True":
            header_line = f.readline().strip()  # Read and discard header

        for line in f:
            parsed_line = {}
            start = 0
            for i, field in enumerate(column_names):
                end = start + offsets[i]
                parsed_line[field] = line[start:end].strip()
                start = end
            parsed_data.append(parsed_line)
    
    return parsed_data


def write_to_csv(parsed_data, output_file, encoding="utf-8"):
    with open(output_file, 'w', newline='', encoding=encoding) as csvfile:
        fieldnames = parsed_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in parsed_data:
            writer.writerow(row)


def main(spec_file, fixed_width_file, output_csv_file):
    spec = load_spec(spec_file)
    parsed_data = parse_fixed_width(fixed_width_file, spec)
    write_to_csv(parsed_data, output_csv_file, spec["DelimitedEncoding"])

if __name__ == "__main__":
    main(SPEC_FILE, INPUT_FILE , OUTPUT_FILE)