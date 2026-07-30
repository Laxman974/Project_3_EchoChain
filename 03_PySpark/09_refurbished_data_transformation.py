from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, regexp_replace

# Create Spark Session
spark = SparkSession.builder \
    .appName("Refurbished Laptop Feature Engineering") \
    .getOrCreate()

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

print("Dataset Loaded Successfully")
df.show(5)


df = df.withColumn(
    "Screen_size",
    regexp_replace(col("Screen_size"), '"', "")
)


df = df.withColumn(
    "Screen_size",
    col("Screen_size").cast("double")
)

print("Screen Size Transformed")
df.select("Screen_size").show(10)

print("Converting Data Types...")

df = df.withColumn("Model_year", col("Model_year").cast("int"))
df = df.withColumn("Memory_GB", col("Memory_GB").cast("int"))
df = df.withColumn("Storage_GB", col("Storage_GB").cast("int"))
df = df.withColumn("Screen_size", col("Screen_size").cast("double"))
df = df.withColumn("Price_euro", col("Price_euro").cast("double"))

print("Data Types Converted")
df.printSchema()

print("Saving Transformed Dataset...")

df.write.mode("overwrite").option("header", True).csv(
    "./01_Dataset/refurbished_laptops_transformed"
)

print("Transformed Dataset Saved Successfully")
spark.stop()
