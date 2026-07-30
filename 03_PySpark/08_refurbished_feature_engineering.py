from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

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
# Create Laptop_Age Column
df = df.withColumn(
    "Laptop_Age",
    lit(2026) - col("Model_year")
)

print("Laptop Age Added")
df.select("Model_year", "Laptop_Age").show(10)

# Create Price_Category Column
df = df.withColumn(
    "Price_Category",
    when(col("Price_euro") < 400, "Budget")
    .when((col("Price_euro") >= 400) & (col("Price_euro") < 800), "Mid Range")
    .otherwise("Premium")
)

print("Price Category Added")
df.select("Price_euro", "Price_Category").show(10)

# Create Storage_Category Column
df = df.withColumn(
    "Storage_Category",
    when(col("Storage_GB") <= 256, "Low Storage")
    .when((col("Storage_GB") > 256) & (col("Storage_GB") <= 512), "Medium Storage")
    .otherwise("High Storage")
)

print("Storage Category Added")
df.select("Storage_GB", "Storage_Category").show(10)

