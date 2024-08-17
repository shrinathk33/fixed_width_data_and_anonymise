import csv
import random
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()

# Filepath for the generated CSV
csv_file_path = 'sample_data.csv'

# Number of rows to generate for the CSV
num_rows = 100*1000

# Column names
columns = ['first_name', 'last_name', 'address', 'date_of_birth']

# Generate the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)  # Write the header
    for _ in range(num_rows):
        writer.writerow([
            fake.first_name(),
            fake.last_name(),
            fake.address().replace("\n", ", "),
            fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
        ])

csv_file_path
