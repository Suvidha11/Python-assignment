import mysql.connector

# Connect to the "Student" database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Student"
)

mycursor = db_connection.cursor()

delete_data = """
DELETE FROM students
WHERE last_name = %s
"""
student_to_delete = ("Smith",)
mycursor.execute(delete_data, student_to_delete)
db_connection.commit()
print("Deleted......")
