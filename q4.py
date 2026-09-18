import pandas as pd

# Question 4: Drop Columns

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Remove the completely empty row
df = df.dropna(how="all")
df = df.reset_index(drop=True)

print("Columns in the dataset:")
print(df.columns.tolist())

print("\nNo columns were dropped.")
print("Reason: All columns contain useful information about orders,")
print("customers, products, sales, profit, or discounts.")