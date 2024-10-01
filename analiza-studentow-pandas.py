import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 


grade_mask = df["Grade"] > 80
subject_mask = df["Subject"].isin(["Math", "Physics"])

# print(df[["Name", "Age"]][subject_mask][grade_mask])
print(df.loc[subject_mask & grade_mask, ["Name", "Age"]])
