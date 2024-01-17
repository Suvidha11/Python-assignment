import mysql.connector

# Connect to the "Student" database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Student"
)
mycursor = db_connection.cursor()

# Display data
display = "SELECT * FROM students"
mycursor.execute(display)
student_records = mycursor.fetchall()

if not student_records:
    print("No student records found.")
else:
    for record in student_records:
        print(record)
