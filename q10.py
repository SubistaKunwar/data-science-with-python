import pandas as pd

# Question 10: Final Clean Dataset

df = pd.read_csv("pandas_dataset.csv")

# Shape before cleaning
before_shape = df.shape

print("Shape before cleaning:")
print(before_shape)


# Remove completely empty rows
df = df.dropna(how="all")

df = df.reset_index(drop=True)

df = df.dropna(subset=["sales"])

df["profit"] = df["profit"].fillna(df["profit"].mean())

df["discount"] = df["discount"].fillna(df["discount"].median())

df["customer_name"] = df["customer_name"].fillna("Unknown")

# Remove duplicate Order IDs
df = df.drop_duplicates(
    subset=["order_id"],
    keep="first"
)

# Reset index again
df = df.reset_index(drop=True)

# Create total_amount
df["total_amount"] = (
    df["quantity"] * df["unit_price"]
    - df["discount"]
)

# Create customer_type
df["customer_type"] = df["quantity"].apply(
    lambda x: "Bulk Buyer" if x >= 3 else "Regular Buyer"
)

after_shape = df.shape

print("\nShape after cleaning:")
print(after_shape)
print("\nFirst 10 rows of cleaned dataset:")
print(df.head(10))