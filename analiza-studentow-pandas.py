import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))
#
#
#

# Oblicz całkowitą wartość sprzedaży
df['total_sales'] = df['price'] * df['quantity']

# Konwersja daty do formatu daty
df['date'] = pd.to_datetime(df['date'])

# Grupowanie danych według miesiąca i produktu

df['month'] = df['date'].dt.to_period('M')

print(df.groupby(['month', 'product'])['total_sales'].sum())