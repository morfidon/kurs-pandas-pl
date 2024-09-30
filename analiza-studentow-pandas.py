import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 

print(df["Grade"] > 90) # Series

