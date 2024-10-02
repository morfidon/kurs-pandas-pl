import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))


# -1 do 1
correlation = df['price'].corr(df['quantity'])
print(f"\n8. Correlation between price and quantity: {correlation:.2f}")