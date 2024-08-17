import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define chunk size for processing (adjustable)
chunk_size = 100000  # Number of rows per chunk

# File paths
input_file = 'sample_data.csv'  # This would be your 2GB file
output_file = 'anonymized_large_file.csv'

# Initialize the CSV writer for the output file
with open(output_file, 'w', newline='') as output:
    writer = None
    
    for chunk in pd.read_csv(input_file, chunksize=chunk_size):
        # Anonymize the data
        chunk['first_name'] = chunk['first_name'].apply(lambda x: fake.first_name())
        chunk['last_name'] = chunk['last_name'].apply(lambda x: fake.last_name())
        chunk['address'] = chunk['address'].apply(lambda x: fake.address().replace("\n", ", "))
        
        # Append the chunk to the output file
        if writer is None:
            writer = chunk.to_csv(output, index=False)
        else:
            chunk.to_csv(output, index=False, header=False, mode='a')
