import mysql.connector

# Connect to the "Student" database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Student"
)
mycursor = db_connection.cursor()

# Create the "students" table
create_table = """
    CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
"""

mycursor.execute(create_table)
print("Table created...")

