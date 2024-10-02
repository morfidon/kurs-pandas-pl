import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")



product_counts = df["product"].value_counts(dropna=False)
quantity_sold = df.groupby("product")["quantity"].sum()

print(quantity_sold)