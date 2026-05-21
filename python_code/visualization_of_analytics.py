import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
students_df = pd.read_csv('data/students.csv')

# -------------------------------
# SHOWING BAR CHART - Student Marks
# -------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    students_df['name'],
    students_df['marks']
)

plt.title('Student Marks Analysis')
plt.xlabel('Student Name')
plt.ylabel('Marks')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# -------------------------------
# SHOWING PIE CHART - Department Distribution
# -------------------------------

department_counts = students_df['department'].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    department_counts,
    labels=department_counts.index,
    autopct='%1.1f%%'
)

plt.title('Department-wise Student Distribution')

plt.show()