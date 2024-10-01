import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 


grade_mask = df["Grade"] > 80
# subject_mask = (df["Subject"] == "Math") | (df["Subject"] == "Physics")

subject_mask = df["Subject"].isin(["Math", "Physics"])


print(df[subject_mask])
