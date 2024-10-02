import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))
#
#
#

# Oblicz całkowitą wartość sprzedaży
df['total'] = df['price'] * df['quantity']


df['date'] = pd.to_datetime(df['date'])

df['day_of_week'] = df['date'].dt.day_name()
#wartosc sprzedazy wedlug dni tygodnia
sale_by_day = df.groupby('day_of_week')['total'].sum()
print(sale_by_day)
