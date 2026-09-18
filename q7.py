import pandas as pd

# Question 7: Handle Missing Customer Name

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

df = df.dropna(how="all")
df = df.reset_index(drop=True)

df["customer_name"] = df["customer_name"].fillna("Unknown")

print("Customer names after handling missing values:")
print(df["customer_name"])