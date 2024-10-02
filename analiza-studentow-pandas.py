import pandas as pd
import matplotlib.pyplot as plt

retrieved_data = {
    'Name': ['Tom', 'Mia', 'Liam', 'Sophia', 'Jake', 'Olivia'],
    'Age': [20, 23, 22, 21, 24, 20],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'Math'],
    'Grade': [75, 82, 68, 90, 88, 65]
} #Dane z innego miejsca

df = pd.read_csv("students.csv") # Data Frame 

df = pd.concat([df, pd.DataFrame(retrieved_data)], ignore_index=True)


# loc (etykietach) oraz iloc (integer) - to do wyborow wielu elementow
# at                    iat (integer) - do pojedynczych wyborow - bo szybsze
print(df)
print(df.iat[0, 0])
