from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, max, min

# Create Spark Session
spark = SparkSession.builder \
    .appName("Refurbished Laptop Data Aggregation") \
    .getOrCreate()

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

print("Dataset Loaded Successfully")
df.show(5)

# ---------------------------------------------
# Average Price by Grade
# ---------------------------------------------
print("Average Price by Grade")

df.groupBy("Grade") \
    .agg(avg("Price_euro").alias("Average_Price")) \
    .show()

# ---------------------------------------------
# Average Price by Storage Type
# ---------------------------------------------
print("Average Price by Storage Type")

df.groupBy("Storage_type") \
    .agg(avg("Price_euro").alias("Average_Price")) \
    .show()

# ---------------------------------------------
# Count of Memory Types
# ---------------------------------------------
print("Memory Type Count")

df.groupBy("Memory_type") \
    .agg(count("*").alias("Total_Count")) \
    .show()

# ---------------------------------------------
# Count of Laptop Grades
# ---------------------------------------------
print("Laptop Grade Count")

df.groupBy("Grade") \
    .agg(count("*").alias("Total_Laptops")) \
    .show()

# ---------------------------------------------
# Maximum Price
# ---------------------------------------------
print("Maximum Laptop Price")

df.select(max("Price_euro").alias("Maximum_Price")) \
    .show()

# ---------------------------------------------
# Minimum Price
# ---------------------------------------------
print("Minimum Laptop Price")

df.select(min("Price_euro").alias("Minimum_Price")) \
    .show()

print("Aggregation Completed Successfully")

spark.stop()