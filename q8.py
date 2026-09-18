import pandas as pd

# Question 8: Detect and Remove Duplicates

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Remove the completely empty row
df = df.dropna(how="all")
df = df.reset_index(drop=True)

# Check for duplicate Order IDs
duplicates = df.duplicated(subset=["order_id"])

print("Duplicate rows:")
print(df[duplicates])

# Count duplicate rows
duplicate_count = duplicates.sum()

print("\nNumber of duplicate rows removed:", duplicate_count)

# Remove duplicate Order IDs
df = df.drop_duplicates(
    subset=["order_id"],
    keep="first"
)

# Reset index
df = df.reset_index(drop=True)

print("\nDataset after removing duplicates:")
print(df)