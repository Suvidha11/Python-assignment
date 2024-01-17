import mysql.connector

# Connect to the "Student" database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Student"
)
mycursor = db_connection.cursor()

# Update the grade of the student named "Alice"
update_data = "UPDATE students SET grade = %s WHERE first_name = %s"
updated_grade = (97.0, "Alice")
mycursor.execute(update_data, updated_grade)

# Commit the changes to the database
db_connection.commit()

print("Grade updated successfully")

