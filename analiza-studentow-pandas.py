import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")

# missing_percentage = (df.isnull().sum() / len(df)) * 100

# # print(missing_percentage.round(2))
# missing_df = missing_percentage.round(2).to_frame(name='Missing data (%)')
# print(missing_df)

print(df["product"].value_counts(dropna=False))