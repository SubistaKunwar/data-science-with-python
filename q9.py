import pandas as pd

# Question 9: Filtering and Creating New Columns

# Read the CSV file
df = pd.read_csv("pandas_dataset.csv")

# Remove the completely empty row
df = df.dropna(how="all")
df = df.reset_index(drop=True)

# 9(a) 

print("Orders where unit_price > 20,000:")

orders_above_20000 = df[df["unit_price"] > 20000]

print(orders_above_20000)

# 9(b) 

print("\nCompleted orders with unit_price > 10,000:")

completed_orders = df[
    (df["unit_price"] > 10000) &
    (df["status"] == "Completed")
]

print(
    completed_orders[
        ["customer_name", "category", "status"]
    ]
)

# 9(c) 

df["total_amount"] = (
    df["quantity"] * df["unit_price"]
    - df["discount"]
)

print("\nDataset with total_amount:")
print(
    df[
        ["quantity", "unit_price", "discount", "total_amount"]
    ]
)

# 9(d) 

df["customer_type"] = df["quantity"].apply(
    lambda x: "Bulk Buyer" if x >= 3 else "Regular Buyer"
)

print("\nDataset with customer_type:")
print(
    df[
        ["customer_name", "quantity", "customer_type"]
    ]
)