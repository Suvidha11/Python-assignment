import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
mycursor = db_connection.cursor()
try:
    mycursor.execute("CREATE DATABASE Student")
    print("DataBase Created.....")
except:
    print("DataBase exit...")
    
