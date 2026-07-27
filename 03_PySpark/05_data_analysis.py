import pandas as pd

df = pd.read_csv("01_Dataset/transformed_products.csv")

print("Average Price:")
print(df["Price"].mean())

print("\nMaximum Price:")
print(df["Price"].max())

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nRAM Distribution:")
print(df["RAM_Size"].value_counts())

print("\nSSD Distribution:")
print(df["SSD_Size"].value_counts())