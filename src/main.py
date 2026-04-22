import os
from db import get_connection
# comment
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


def main():
    launch()
    while True:
        print("\nClub Management System")
        print("1. List all clubs")
        print("2. Add a student")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_clubs()
        elif choice == "2":
            add_student()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()