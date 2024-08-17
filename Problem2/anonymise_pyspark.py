from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from faker import Faker

# Initialize Spark session
spark = SparkSession.builder.appName("Anonymize Data").getOrCreate()

# Initialize Faker
fake = Faker()

# Load the CSV file
df = spark.read.csv('sample_data.csv', header=True)

# Define UDFs for anonymization
fake_first_name = udf(lambda: fake.first_name())
fake_last_name = udf(lambda: fake.last_name())
fake_address = udf(lambda: fake.address().replace("\n", ", "))

# Apply UDFs to anonymize columns
df = df.withColumn("first_name", fake_first_name()) \
       .withColumn("last_name", fake_last_name()) \
       .withColumn("address", fake_address())

# Save the anonymized data
df.write.csv('anonymized_very_large_file_spark.csv', header=True)

# Stop the Spark session
spark.stop()
