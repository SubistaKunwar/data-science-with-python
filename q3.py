import pandas as pd

# Question 3: Drop unnecessary rows

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Display the dataset before cleaning
print("Before removing empty rows:")
print(df.head())

# Remove rows where all values are missing
df = df.dropna(how="all")

df = df.reset_index(drop=True)

print("\nAfter removing empty rows:")
print(df.head())