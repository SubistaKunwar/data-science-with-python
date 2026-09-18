import pandas as pd

# Question 5: Count Missing Values

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Remove the completely empty row
df = df.dropna(how="all")
df = df.reset_index(drop=True)

missing_values = df.isnull().sum()

print("Missing values in each column:")
print(missing_values)