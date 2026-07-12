import pandas as pd

# Read the dataset
df = pd.read_csv("01_Dataset/products.csv")

# Display the first 5 rows
print("\n===== First 5 Rows =====")
print(df.head())

# Dataset information
print("\n===== Dataset Information =====")
print(df.info())

# Dataset shape
print("\n===== Dataset Shape =====")
print(df.shape)

# Column names
print("\n===== Column Names =====")
print(df.columns)

# Missing values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# Duplicate records
print("\n===== Duplicate Records =====")
print(df.duplicated().sum())

# Statistical summary
print("\n===== Statistical Summary =====")
print(df.describe(include="all"))