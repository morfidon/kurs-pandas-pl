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

# Konwersja daty do formatu daty
df['date'] = pd.to_datetime(df['date'])

# Najlepsza sprzedaż (kiedy)

print(df.groupby('date')['total'].sum().idxmax(), df.groupby('date')['total'].sum().max())

# Najgorsza sprzedaż (kiedy)
print(df.groupby('date')['total'].sum().idxmin(), df.groupby('date')['total'].sum().min())
