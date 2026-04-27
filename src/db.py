import mysql.connector
import getpass

# Use a dictionary to store state instead of separate global variables.
_credentials = {
    "user": None,
    "password": None
}

def get_connection():
    # Check if the dictionary values are empty
    if not _credentials["user"] or not _credentials["password"]:
        print("\nEnter MySQL credentials:")
        
        # Keep prompting until a valid string is entered
        while not _credentials["user"]:
            _credentials["user"] = input("Username: ").strip()
            
        while not _credentials["password"]:
            _credentials["password"] = getpass.getpass("Password: ").strip()

    return mysql.connector.connect(
        host="mysql.cs.uky.edu",     
        user=_credentials["user"],
        password=_credentials["password"],
        database=_credentials["user"]  
    )

def wipe_credentials():
    """Clears the dictionary when the user exits."""
    _credentials["user"] = None
    _credentials["password"] = None