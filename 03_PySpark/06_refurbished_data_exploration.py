from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Refurbished Laptop Data Exploration") \
    .getOrCreate()

# Load Dataset
df = spark.read.csv(
    "01_Dataset/refurbished_laptops.csv",
    header=True,
    inferSchema=True
)

print("First 5 Rows")
df.show(5)

print("Schema")
df.printSchema()

print("Total Rows:", df.count())
print("Total Columns:", len(df.columns))

print("Columns")
print(df.columns)

print("Summary Statistics")
df.describe().show()

spark.stop()