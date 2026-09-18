import pandas as pd

# Question 6: Handle Missing Values

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Remove the completely empty row
df = df.dropna(how="all")
df = df.reset_index(drop=True)

# Q6(a)

df = df.dropna(subset=["sales"])
print("After dropping rows with missing sales:")
print(df)

# Q6(b): 

profit_mean = df["profit"].mean()
df["profit"] = df["profit"].fillna(profit_mean)
discount_median = df["discount"].median()
df["discount"] = df["discount"].fillna(discount_median)

print("\nMean profit used:", profit_mean)
print("Median discount used:", discount_median)
print("\nAfter filling missing profit and discount:")
print(df[["profit", "discount"]])