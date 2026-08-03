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

# ----------------------------------------
# Remove Duplicate Rows
# ----------------------------------------
df = df.dropDuplicates()

# ----------------------------------------
# Remove Rows with Null Values
# ----------------------------------------
df = df.dropna()

print("Rows After Cleaning:", df.count())

# ----------------------------------------
# Check Null Values
# ----------------------------------------
print("\nNull Values:")
for column in df.columns:
    print(column, ":", df.filter(col(column).isNull()).count())

# ----------------------------------------
# Convert Euro to Indian Rupees
# ----------------------------------------

EXCHANGE_RATE = 100   # 1 Euro = ₹100

df = df.withColumn(
    "Price_INR",
    col("Price_euro") * EXCHANGE_RATE
)

print("\nPrice Converted to INR")
df.select("Price_euro", "Price_INR").show(10)

# ----------------------------------------
# Show Cleaned Data
# ----------------------------------------

print("\nCleaned Data:")
df.show(5)

# ----------------------------------------
# Save Cleaned Dataset
# ----------------------------------------

df.toPandas().to_csv(
    "01_Dataset/cleaned_refurbished_laptops.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

spark.stop()