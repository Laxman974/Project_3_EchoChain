from pyspark.sql import SparkSession

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Refurbished Laptop Data Exploration")
    .getOrCreate()
)

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

# Show first 5 rows
print("===== First 5 Rows =====")
df.show(5)

# Print Schema
print("===== Schema =====")
df.printSchema()

# Total Rows and Columns
print("Total Rows:", df.count())
print("Total Columns:", len(df.columns))

# Column Names
print("\n===== Column Names =====")
print(df.columns)

# Summary Statistics
print("\n===== Summary Statistics =====")
df.describe().show()

# Count by Grade
print("\n===== Grade Distribution =====")
df.groupBy("Grade").count().show()

# Count by Storage Type
print("\n===== Storage Type Distribution =====")
df.groupBy("Storage_type").count().show()

# Count by Memory Type
print("\n===== Memory Type Distribution =====")
df.groupBy("Memory_type").count().show()

# Average Price
print("\n===== Average Price =====")
df.selectExpr("avg(Price_euro) as Average_Price").show()

# Maximum Price
print("\n===== Maximum Price =====")
df.selectExpr("max(Price_euro) as Maximum_Price").show()

# Minimum Price
print("\n===== Minimum Price =====")
df.selectExpr("min(Price_euro) as Minimum_Price").show()

spark.stop()