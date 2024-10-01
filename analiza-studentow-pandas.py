import pandas as pd
retrieved_data = {
    'Name': ['Tom', 'Mia', 'Liam', 'Sophia', 'Jake', 'Olivia'],
    'Age': [20, 23, 22, 21, 24, 20],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'Math'],
    'Grade': [75, 82, 68, 90, 88, 65]
} #Dane z innego miejsca

df = pd.read_csv("students.csv") # Data Frame 

result = pd.concat([df, pd.DataFrame(retrieved_data)], ignore_index=True)


print(result)

