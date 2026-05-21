import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('database/university_dashboard.db')

# Load dataset
students_df = pd.read_csv('data/students.csv')

# Store dataset into SQLite table
students_df.to_sql(
    'student_performance',
    conn,
    if_exists='replace',
    index=False
)

print("University student data now loaded into SQLite database successfully")

# Close connection
conn.close()