import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))
#
#


# Dzienna częstotliwość sprzedaży
df['date'] = pd.to_datetime(df['date'])
print(df["date"].value_counts().sort_index())