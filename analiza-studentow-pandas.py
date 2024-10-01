import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 


print(df[["Name", "Age", "Grade"]])
