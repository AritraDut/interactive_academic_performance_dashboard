import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('database/university_dashboard.db')

# Load table data
query = "SELECT * FROM student_performance"

students_df = pd.read_sql_query(query, conn)

print("Student Performance Data:\\n")
print(students_df)

# KPI Calculations
average_marks = students_df['marks'].mean()
average_attendance = students_df['attendance_percentage'].mean()
highest_cgpa = students_df['cgpa'].max()
lowest_cgpa = students_df['cgpa'].min()

print("\\nKey Performance Indicators are showed below\\n")

print("Average Marks:", round(average_marks, 2))
print("Average Attendance:", round(average_attendance, 2))
print("Highest CGPA:", highest_cgpa)
print("Lowest CGPA:", lowest_cgpa)

# Average Marks Department wise
department_analysis = students_df.groupby('department')['marks'].mean()

print("\\nDepartment-wise Average Marks:\\n")
print(department_analysis)

# Close connection
conn.close()

print("\\nStudent Analytics Process Completed Successfully")