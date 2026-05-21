import pandas as pd

# Load student dataset
students_df = pd.read_csv('data/students.csv')

# Display dataset
print("Student Dataset Loaded Successfully")
print("\nStudent Records:\n")

print(students_df)

# Display dataset information
print("\nDataset Information:\n")
students_df.info()