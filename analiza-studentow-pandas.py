import pandas as pd
retrieved_data = {
    'Name': ['Tom', 'Mia', 'Liam', 'Sophia', 'Jake', 'Olivia'],
    'Age': [20, 23, 22, 21, 24, 20],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'Math'],
    'Grade': [75, 82, 68, 90, 88, 65]
} #Dane z innego miejsca

df = pd.read_csv("students.csv") # Data Frame 

result = pd.concat([df, pd.DataFrame(retrieved_data)], ignore_index=True)


# result = result.groupby("Subject")["Grade"].mean().reset_index(name="Average Grade")
# result = result.groupby("Subject")["Age"].max().reset_index(name="Max Age")
# result = result.groupby("Subject").size().reset_index(name="Amount of students")

result = result.groupby("Subject").agg(
    AverageGrade=("Grade", "mean"),
    MaxAge=("Age", "max"),
    AmountOfStudents=("Name", "count")
).reset_index()

# result = result.rename(columns={
#     "MaxAge": "Maksymalny Wiek",
#     "Subject": "Przedmiot"
# })
result.columns = ["Subject", "Average Grade", "Max Age", "Amount Of Students"]
print(result)
