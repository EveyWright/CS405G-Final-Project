import mysql.connector
import getpass

_connection = None

def get_connection():
    global _connection
    if _connection is None or not _connection.is_connected():
        print("Enter MySQL credentials:")
        user = input("Username: ")
        password = getpass.getpass("Password: ")
        _connection = mysql.connector.connect(
            host="mysql.cs.uky.edu",
            user=user,
            password=password,
            database=user
        )
    return _connection
