import pandas as pd

df = pd.read_csv("students.csv") # Data Frame 

#mask 
grade_mask = df["Grade"] > 80
subject_mask = df["Subject"] == "Math"
# or and  | &
# True False
# 

print(grade_mask)
print(subject_mask)
'''
     True
    False
     True
     True
     True

     True
    False
     True
    False
    False

    & - koniunkcja - tylko wtedy, gdy OBA WARUNKI są prawdziwe
    True
    False
    True
    False
    False

    | - or - lub - alternatywa jest fałszywa, TYLKO wtedy GDY OBA warunki są fałszywe
    True
    False
    True
    True
    True

    xor - ^
    ~ 

'''
print(df[grade_mask & subject_mask])
