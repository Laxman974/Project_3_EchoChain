import pandas as pd

# Load dataset
df = pd.read_csv("01_Dataset/products.csv")

print("===== Missing Values Before Cleaning =====")
print(df.isnull().sum())

print("\n===== Duplicate Records Before Cleaning =====")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
df["Warranty"] = df["Warranty"].fillna("No Warranty")
df["OS"] = df["OS"].fillna("Unknown OS")

# Remove unnecessary column (if present)
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(
    "01_Dataset/cleaned_products.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as cleaned_products.csv")

df = pd.read_csv("01_Dataset/cleaned_products.csv", encoding="utf-8-sig")
print(df.head(5))