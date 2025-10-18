import mysql.connector
from mysql.connector import Error

mydb = None
mycursor = None
try:
    # Database connection details
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sample",
        database="alx_book_store"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Create a Database (if it doesn't exist)
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")
        mydb.commit()

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close connections
    if mycursor is not None:
        mycursor.close()
    if mydb is not None:
        mydb.close()

