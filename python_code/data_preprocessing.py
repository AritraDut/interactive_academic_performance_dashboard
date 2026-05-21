import pandas as pd

# Load dataset
students_df = pd.read_csv('data/students.csv')

print("Original Dataset:\n")
print(students_df)

# Remove duplicate rows
students_df.drop_duplicates(inplace=True)

# Handle missing values
students_df.fillna(0, inplace=True)

# Convert column names to lowercase
students_df.columns = students_df.columns.str.lower()

print("\nCleaned Dataset:\n")
print(students_df)

print("\nData Preprocessing Completed Successfully")