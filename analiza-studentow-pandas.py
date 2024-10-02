import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

product_counts = df["product"].value_counts(dropna=False)
quantity_sold = df.groupby("product")["quantity"].sum()
print(product_counts)
print(quantity_sold)

comparison_df = pd.DataFrame(
    {
        "Transaction Count": product_counts,
        "Total Quantity": quantity_sold
    }
)
print(comparison_df)