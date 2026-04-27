import os
from db import get_connection, wipe_credentials

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
    conn.commit()

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
    year = int(input("Year: "))
    sql = """
        SELECT club_name FROM Advises
        WHERE faculty_ID = %s AND year = %s
    """
    cursor.execute(sql, (faculty_id, year))
    print("\nClubs advised by faculty member:")
    for row in cursor:
        print(row[0])
    print("\nNumber of rows:", cursor.rowcount)
    cursor.close()
    conn.close()

# get faculty ID by name
def get_faculty_id_by_name():
    conn = get_connection()
    cursor = conn.cursor()
    name = input("Faculty name: ").strip()
    sql = "SELECT faculty_ID FROM Faculty WHERE name = %s"
    cursor.execute(sql, (name,))
    results = cursor.fetchall()
    if results:
        print("Faculty ID(s):")
        for row in results:
            print(row[0])
    else:
        print("Faculty member not found.")
    cursor.close()
    conn.close()

def join_or_leave_club():
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("student ID: "))
    club_name = input("Club name: ")
    year = int(input("Year: "))
    print("1. Join  2. Leave")
    choice = input("Choose: ")
    if choice == "1":
        sql = "INSERT IGNORE INTO Member (student_ID, club_name, year) VALUES (%s, %s, %s)"
        cursor.execute(sql, (student_id, club_name, year))
        print("Student joined successfully.")
    elif choice == "2":
        sql = "DELETE FROM Member WHERE student_ID = %s AND club_name = %s AND year = %s"
        cursor.execute(sql, (student_id, club_name, year))
        print("Student left successfully.")
    conn.commit()
    
    

def list_club_members():
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("Club name: ")
    year = int(input("Year: "))
    sql = """
        SELECT s.name FROM Student s
        JOIN Member m ON s.student_ID = m.student_ID
        WHERE m.club_name = %s AND m.year = %s
    """
    cursor.execute(sql, (club_name, year))
    print("\nMembers:")
    for row in cursor:
        print(row[0])
    
    

def list_student_clubs():
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("Student ID: "))
    year = int(input("Year: "))
    sql = "SELECT club_name FROM Member WHERE student_ID = %s AND year = %s"
    cursor.execute(sql, (student_id, year))
    print("\nClubs:")
    for row in cursor:
        print(row[0])
    
    

def student_schedule_on_date():
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("Student ID: "))
    date = input("Date (YYYY-MM-DD): ")
    print("\n-- Meetings --")
    sql = """
        SELECT e.club_name, e.time, m.classroom, e.description
        FROM Meeting m
        JOIN Event e ON m.event_ID = e.event_ID
        JOIN Member mb ON e.club_name = mb.club_name AND YEAR(e.date) = mb.year
        WHERE mb.student_ID = %s AND e.date = %s
    """
    cursor.execute(sql, (student_id, date))
    for row in cursor:
        hours, remainder = divmod(row[1].seconds, 3600)
        minutes = remainder // 60
        print(f"Club: {row[0]} | Time: {hours:02}:{minutes:02} | Classroom: {row[2]} | Description: {row[3]}")
    print("\n-- Events --")
    sql = """
        SELECT e.club_name, e.time, e.description
        FROM Field_Trip ft
        JOIN Event e ON ft.event_ID = e.event_ID
        JOIN Member mb ON e.club_name = mb.club_name AND YEAR(e.date) = mb.year
        WHERE mb.student_ID = %s AND e.date = %s
    """
    cursor.execute(sql, (student_id, date))
    for row in cursor:
        print(row)
    
def add_event():
    conn = get_connection()
    cursor = conn.cursor()
    
    event_id = int(input("Event ID: "))
    club_name = input("Club Name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM:SS): ")
    description = input("Description: ")
    event_type = input("Is this a Meeting (M) or Field Trip (F)? ").strip().upper()

    try:
        # Insert into parent Event table
        cursor.execute("""
            INSERT INTO Event (event_ID, club_name, date, time, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (event_id, club_name, date, time, description))
        
        # Insert into specific child table
        if event_type == 'M':
            classroom = input("Classroom: ")
            cursor.execute("INSERT INTO Meeting (event_ID, classroom) VALUES (%s, %s)", (event_id, classroom))
        elif event_type == 'F':
            location = input("Location: ")
            cursor.execute("INSERT INTO Field_Trip (event_ID, location) VALUES (%s, %s)", (event_id, location))
            
        conn.commit()
        print("Event added successfully.")
    except Exception as e:
        print(f"Error adding event: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_event():
    conn = get_connection()
    cursor = conn.cursor()
    event_id = int(input("Enter Event ID to delete: "))
    
    try:
        # Must delete from child tables first due to foreign key constraints
        cursor.execute("DELETE FROM Meeting WHERE event_ID = %s", (event_id,))
        cursor.execute("DELETE FROM Field_Trip WHERE event_ID = %s", (event_id,))
        # Now delete from parent table
        cursor.execute("DELETE FROM Event WHERE event_ID = %s", (event_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print("Event deleted successfully.")
        else:
            print("Event not found.")
    except Exception as e:
        print(f"Error deleting event: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def view_club_students():
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("Club Name: ")
    year = int(input("Year: "))
    
    sql = """
        SELECT s.student_ID, s.name, s.grade 
        FROM Student s
        JOIN Member m ON s.student_ID = m.student_ID
        WHERE m.club_name = %s AND m.year = %s
    """
    cursor.execute(sql, (club_name, year))
    results = cursor.fetchall()
    
    print(f"\nStudents in {club_name} ({year}):")
    if results:
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]}")
    else:
        print("No students found.")
        
    cursor.close()
    conn.close()

def view_clubs_advisors():
    conn = get_connection()
    cursor = conn.cursor()
    year = int(input("Year: "))
    
    sql = """
        SELECT a.club_name, f.name, f.dept
        FROM Advises a
        JOIN Faculty f ON a.faculty_ID = f.faculty_ID
        WHERE a.year = %s
    """
    cursor.execute(sql, (year,))
    results = cursor.fetchall()
    
    print(f"\nClubs and Advisors ({year}):")
    if results:
        for row in results:
            print(f"Club: {row[0]} | Advisor: {row[1]} ({row[2]})")
    else:
        print("No records found.")
        
    cursor.close()
    conn.close()
    

def add_event():
    conn = get_connection()
    cursor = conn.cursor()
    
    event_id = int(input("Event ID: "))
    club_name = input("Club Name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM:SS): ")
    description = input("Description: ")
    event_type = input("Is this a Meeting (M) or Field Trip (F)? ").strip().upper()

    try:
        # Insert into parent Event table
        cursor.execute("""
            INSERT INTO Event (event_ID, club_name, date, time, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (event_id, club_name, date, time, description))
        
        # Insert into specific child table
        if event_type == 'M':
            classroom = input("Classroom: ")
            cursor.execute("INSERT INTO Meeting (event_ID, classroom) VALUES (%s, %s)", (event_id, classroom))
        elif event_type == 'F':
            location = input("Location: ")
            cursor.execute("INSERT INTO Field_Trip (event_ID, location) VALUES (%s, %s)", (event_id, location))
            
        conn.commit()
        print("Event added successfully.")
    except Exception as e:
        print(f"Error adding event: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_event():
    conn = get_connection()
    cursor = conn.cursor()
    event_id = int(input("Enter Event ID to delete: "))
    
    try:
        # Must delete from child tables first due to foreign key constraints
        cursor.execute("DELETE FROM Meeting WHERE event_ID = %s", (event_id,))
        cursor.execute("DELETE FROM Field_Trip WHERE event_ID = %s", (event_id,))
        # Now delete from parent table
        cursor.execute("DELETE FROM Event WHERE event_ID = %s", (event_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print("Event deleted successfully.")
        else:
            print("Event not found.")
    except Exception as e:
        print(f"Error deleting event: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def view_clubs_advisors():
    conn = get_connection()
    cursor = conn.cursor()
    year = int(input("Year: "))
    
    sql = """
        SELECT a.club_name, f.name, f.dept
        FROM Advises a
        JOIN Faculty f ON a.faculty_ID = f.faculty_ID
        WHERE a.year = %s
    """
    cursor.execute(sql, (year,))
    results = cursor.fetchall()
    
    print(f"\nClubs and Advisors ({year}):")
    if results:
        for row in results:
            print(f"Club: {row[0]} | Advisor: {row[1]} ({row[2]})")
    else:
        print("No records found.")
        
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
            print("Club Management")
            print("1. Add an event/meeting")
            print("2. Delete an event/meeting")
            print("1. Add an event/meeting")
            print("2. Delete an event/meeting")
            print("3. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                add_event()
            elif choice == "2":
                delete_event()
            elif choice == "3":
                continue
        elif choice == "2":
            print("Faculty Management")
            print("1. Get Faculty ID by Name")
            print("2. Assign a faculty advisor to a club")
            print("3. List all clubs advised by a faculty member")
            print("4. View all clubs and their advisors in a year")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                get_faculty_id_by_name()
            elif choice == "2":
                assign_advisor()
            elif choice == "3":
                list_advised_clubs()
            elif choice == "4":
                view_clubs_advisors()
            elif choice == "5":
                continue
        
        elif choice == "3":
            print("Student Management")
            print("1. Join or leave a club")
            print("2. List all members of a club")
            print("3. List all clubs a student belongs to")
            print("4. View student schedule on a date")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                join_or_leave_club()
            elif choice == "2":
                list_club_members()
            elif choice == "3":
                list_student_clubs()
            elif choice == "4":
                student_schedule_on_date()
            elif choice == "5":
                continue
        elif choice == "4":
            print("Exiting...")
            wipe_credentials()  # Clear credentials on exit
            print("Wiping credentials and exiting...")
            wipe_credentials()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
