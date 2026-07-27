import pandas as pd

# Load cleaned dataset
df = pd.read_csv("01_Dataset/cleaned_products.csv")

print("===== Dataset Shape =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)

# Future feature engineering steps
# 1. Extract RAM size
# Create a new feature for RAM size
df["RAM_Size"] = df["Ram"].str.extract(r'(\d+)').astype(float)

print(df[["Ram", "RAM_Size"]].head())

# 2. Convert Price column to numeric
# 3. Categorize laptops by price range

print("\nFeature engineering script created successfully!")