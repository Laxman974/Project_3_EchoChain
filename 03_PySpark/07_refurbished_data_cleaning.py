from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("Refurbished Laptop Data Cleaning") \
    .getOrCreate()

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

print("Original Rows:", df.count())

# Remove duplicates
df = df.dropDuplicates()

# Remove rows with null values
df = df.dropna()

print("Rows After Cleaning:", df.count())

# Check null values
for column in df.columns:
    print(column, df.filter(col(column).isNull()).count())

# Show cleaned data
df.show(5)

spark.stop()