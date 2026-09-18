import pandas as pd

# Question 2: Rename columns
df = pd.read_csv("pandas_dataset.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
print("Clean column names:")
print(df.columns)