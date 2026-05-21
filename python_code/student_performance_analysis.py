import pandas as pd

# Load dataset
students_df = pd.read_csv('data/students.csv')

# Create Risk Status Column
students_df['risk_status'] = students_df.apply(
    lambda row: 'At Risk'
    if row['attendance_percentage'] < 75 or row['cgpa'] < 6
    else 'Safe',
    axis=1
)

# Create Grade Category Column
students_df['grade_category'] = pd.cut(
    students_df['marks'],
    bins=[0, 40, 60, 80, 100],
    labels=['Fail', 'Average', 'Good', 'Excellent']
)

# Display Updated Dataset
print("Dataset after adding new columns risk status and grade category:\\n")
print(students_df)

# Display At-Risk Students
print("\\nAt-Risk Students:\\n")

print(
    students_df[
        students_df['risk_status'] == 'At Risk'
    ][['name', 'attendance_percentage', 'cgpa']]
)

print("\\nFeature Engineering Completed Successfully")