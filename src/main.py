import os
from db import get_connection

def launch():
    conn = get_connection()
    cursor = conn.cursor()
    with open(os.path.join(os.path.dirname(__file__), "..", "sql", "schema.sql"), "r") as f:
        sql = f.read()
    
    # Remove SQL comments and split by semicolon
    lines = [line for line in sql.split('\n') if not line.strip().startswith('--')]
    sql = '\n'.join(lines)
    
    # Split statements by semicolon and execute individually
    for statement in sql.split(';'):
        statement = statement.strip()
        if statement:  # Skip empty statements
            cursor.execute(statement)
    
    conn.commit()
    print("Database initialized successfully.")

    with open(os.path.join(os.path.dirname(__file__), "..", "sql", "sample_data.sql"), "r") as f:
        sql = f.read()
    
    # Remove SQL comments and split by semicolon
    lines = [line for line in sql.split('\n') if not line.strip().startswith('--')]
    sql = '\n'.join(lines)
    
    # Split statements by semicolon and execute individually
    for statement in sql.split(';'):
        statement = statement.strip()
        if statement:  # Skip empty statements
            cursor.execute(statement)
    
    conn.commit()
    print("Sample data inserted successfully.")

    cursor.close()
    conn.close()


def list_clubs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM Club")
    print("\nClubs:")
    for row in cursor:
        print(row[0])

    print("\nNumber of rows:", cursor.rowcount)

    cursor.close()
    conn.close()


def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Student ID: "))
    name = input("Name: ")
    grade = int(input("Grade: "))
    parent_number = input("Parent phone number: ")

    sql = """
        INSERT INTO Student (student_ID, name, grade, parent_number)
        VALUES (%s, %s, %s, %s)
    """
    values = (student_id, name, grade, parent_number)

    cursor.execute(sql, values)
    conn.commit()   # IMPORTANT, same as your example

    print("Student added successfully.")

    cursor.close()
    conn.close()

# assign a faculty advisor to a club in a year
def assign_advisor():
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("Club name: ")
    faculty_id = int(input("Faculty ID: "))
    year = int(input("Year: "))
    values = (club_name, faculty_id, year)
    sql = """
        INSERT INTO Advises (club_name, faculty_ID, year)
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, values)
    conn.commit()
    print("Advisor assigned successfully.")
    cursor.close()
    conn.close()

# list all clubs advised by a faculty member
def list_advised_clubs():
    conn = get_connection()
    cursor = conn.cursor()
    faculty_id = int(input("Faculty ID: "))
    sql = """
        SELECT club_name FROM Advises
        WHERE faculty_ID = %s
    """
    cursor.execute(sql, (faculty_id,))
    print("\nClubs advised by faculty member:")
    for row in cursor:
        print(row[0])
    print("\nNumber of rows:", cursor.rowcount)
    cursor.close()
    conn.close()

def main():
    launch()
    while True:
        print("\nClub Management System")
        print("1. Manage Clubs")
        print("2. Manage Faculty")
        print("3. Manage Students")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("1. Option 1")
            print("2. Option 2")
            print("3. Go Back")

            choice = input("Choose an option: ")
            # Implement club management options here
        elif choice == "2":
            print("1. Assign a faculty advisor to a club")
            print("2. List all clubs advised by a faculty member")
            print("3. Go Back")

            choice = input("Choose an option: ")
            # Implement faculty management options here
            if choice == "1":
                assign_advisor()
            elif choice == "2":
                list_advised_clubs()
            elif choice == "3":
                continue
        elif choice == "3":
            print("1. Option 1")
            print("2. Option 2")
            print("3. Go Back")

            choice = input("Choose an option: ")
            # Implement student management options here
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()