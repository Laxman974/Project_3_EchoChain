import pandas as pd

# Load dataset
df = pd.read_csv("01_Dataset/cleaned_products.csv")

print("===== Before Transformation =====")
print(df.head())

# Convert Price into numeric
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"])

# Extract RAM size
df["RAM_Size"] = (
    df["Ram"]
    .astype(str)
    .str.extract(r'(\d+)')
)

df["RAM_Size"] = pd.to_numeric(
    df["RAM_Size"],
    errors="coerce"
)

# Extract SSD size
df["SSD_Size"] = (
    df["SSD"]
    .astype(str)
    .str.extract(r'(\d+)')
)

# Convert 1 TB to 1024 GB
df.loc[
    df["SSD"].astype(str).str.contains(
        "TB",
        case=False,
        na=False
    ),
    "SSD_Size"
] = "1024"

df["SSD_Size"] = pd.to_numeric(
    df["SSD_Size"],
    errors="coerce"
)

print("\n===== After Transformation =====")
print(
    df[
        ["Price", "RAM_Size", "SSD_Size"]
    ].head()
)

# Save transformed dataset
df.to_csv(
    "01_Dataset/transformed_products.csv",
    index=False
)

print("\nTransformation Completed Successfully!")