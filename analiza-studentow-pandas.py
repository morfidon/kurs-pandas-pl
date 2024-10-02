import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")

print(df.isnull().sum()) #null