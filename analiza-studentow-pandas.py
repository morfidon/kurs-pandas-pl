import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 

# print(df["Grade"] > 90) # Series

high_grade_students = df[df["Grade"] > 90]

high_grade_students.to_csv("studenci_wysokie_oceny.csv", index=False)

