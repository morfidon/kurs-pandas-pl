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

# Porównanie sprzedaży między miesiącami w procentach
df['month'] = df['date'].dt.to_period('M')
df_monthly_sales = df.groupby('month')['total'].sum()


# Sprzedaż miesięczna (ile procent jest odpowiedzielne za sprzedaż w danym miesiącu)


#
df_monthly_sales_percent = df_monthly_sales.pct_change() * 100
print(df_monthly_sales_percent)
#NaN - Not Available Number

