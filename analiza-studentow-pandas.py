import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 

df['Missing Points'] = 100 - df['Grade']
print(df)

