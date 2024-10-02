import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))
#
#

avg_price_by_category = df.groupby('category')['price'].mean().sort_values(ascending=False)
print(avg_price_by_category)

plt.figure(figsize=(16, 9))
avg_price_by_category.plot(kind='bar', color='red')
plt.title("Average Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('avg_price_by_category.png')

