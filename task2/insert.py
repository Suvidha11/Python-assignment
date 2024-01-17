import mysql.connector

# Connect to the "Student" database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Student"
)
mycursor = db_connection.cursor()

# Insert a new student record
insert_data = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
student_data = ("Alice", "Smith", 18, 95.5)
mycursor.execute(insert_data, student_data)

# Commit the changes to the database
db_connection.commit()

print("Data inserted successfully")



