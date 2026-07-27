from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Refurbished Laptop Data Cleaning")
    .getOrCreate()
)

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

print("Original Rows:", df.count())

# Remove duplicate rows
df = df.dropDuplicates()

# Remove rows with null values
df = df.dropna()

print("Rows After Cleaning:", df.count())

# Check null values
print("\nNull Values:")
for column in df.columns:
    print(column, ":", df.filter(col(column).isNull()).count())

# Show cleaned data
print("\nCleaned Data:")
df.show(5)

# Save cleaned dataset
df.toPandas().to_csv(
    "01_Dataset/cleaned_refurbished_laptops.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

spark.stop()