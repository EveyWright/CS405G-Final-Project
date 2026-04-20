import mysql.connector
import getpass

def get_connection():
    print("Enter MySQL credentials:")
    user = input("Username: ")
    password = getpass.getpass("Password: ")

    return mysql.connector.connect(
        host="mysql.cs.uky.edu",     # or "localhost"
        user=user,
        password=password,
        database=user  # Assuming the database name is the same as the username
    )