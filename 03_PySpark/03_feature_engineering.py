import pandas as pd

# Load cleaned dataset
df = pd.read_csv("01_Dataset/cleaned_products.csv")

print("===== Dataset Shape =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)

# Future feature engineering steps
# 1. Extract RAM size
# 2. Convert Price column to numeric
# 3. Categorize laptops by price range

print("\nFeature engineering script created successfully!")