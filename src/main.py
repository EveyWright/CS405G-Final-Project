import os
from db import get_connection, wipe_credentials

# ============================================================================
# HELPER FUNCTIONS TO DISPLAY TABLES
# ============================================================================

def show_all_clubs():
    """Display all clubs in a formatted table"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Club ORDER BY name")
    results = cursor.fetchall()
    
    print("\n" + "="*40)
    print("AVAILABLE CLUBS")
    print("="*40)
    if results:
        for row in results:
            print(f"  • {row[0]}")
    else:
        print("  No clubs found.")
    print("="*40)
    
    cursor.close()
    conn.close()

def show_all_faculty():
    """Display all faculty members in a formatted table"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT  name, dept FROM Faculty ORDER BY faculty_ID")
    results = cursor.fetchall()
    
    print("\n" + "="*60)
    print("FACULTY MEMBERS")
    print("="*60)
    print(f"{'Name':<30} {'Department':<20}")
    print("-"*60)
    if results:
        for row in results:
            print(f"{row[0]:<30} {row[1]:<20}")
    else:
        print("No faculty found.")
    print("="*60)
    
    cursor.close()
    conn.close()

def show_all_students():
    """Display all students in a formatted table"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_ID, name, grade FROM Student ORDER BY student_ID")
    results = cursor.fetchall()
    
    print("\n" + "="*50)
    print("STUDENTS")
    print("="*50)
    print(f"{'ID':<10} {'Name':<30} {'Grade':<10}")
    print("-"*50)
    if results:
        for row in results:
            print(f"{row[0]:<10} {row[1]:<30} {row[2]:<10}")
    else:
        print("No students found.")
    print("="*50)
    
    cursor.close()
    conn.close()

def show_all_events():
    """Display all events with IDs for easy deletion/reference"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.event_ID, e.club_name, e.date, e.time, e.description,
               IF(m.event_ID IS NOT NULL, 'Meeting', 'Field Trip') as type
        FROM Event e
        LEFT JOIN Meeting m ON e.event_ID = m.event_ID
        ORDER BY e.date, e.time
    """)
    results = cursor.fetchall()
    
    print("\n" + "="*90)
    print("ALL EVENTS")
    print("="*90)
    print(f"{'ID':<6} {'Club':<15} {'Date':<12} {'Time':<10} {'Type':<12} {'Description':<30}")
    print("-"*90)
    if results:
        for row in results:
            print(f"{row[0]:<6} {row[1]:<15} {str(row[2]):<12} {str(row[3]):<10} {row[5]:<12} {row[4]:<30}")
    else:
        print("No events found.")
    print("="*90)
    
    cursor.close()
    conn.close()

def show_budgets():
    """Display all club budgets"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT club_name, year, total 
        FROM Budget 
        ORDER BY year DESC, club_name
    """)
    results = cursor.fetchall()
    
    print("\n" + "="*60)
    print("CLUB BUDGETS")
    print("="*60)
    print(f"{'Club':<20} {'Year':<10} {'Budget':<15}")
    print("-"*60)
    if results:
        for row in results:
            print(f"{row[0]:<20} {row[1]:<10} ${row[2]:>12.2f}")
    else:
        print("No budgets recorded.")
    print("="*60)
    
    cursor.close()
    conn.close()

def show_student_clubs(student_id, year):
    """Display clubs a specific student is in"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT club_name 
        FROM Member 
        WHERE student_ID = %s AND year = %s
    """, (student_id, year))
    results = cursor.fetchall()
    
    if results:
        print(f"\n  Current clubs for student {student_id} ({year}):")
        for row in results:
            print(f"    • {row[0]}")
    else:
        print(f"\n  Student {student_id} is not in any clubs for {year}.")
    
    cursor.close()
    conn.close()

# ============================================================================

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

    student_id = int(input("Student ID (3-digit number, e.g., 101): "))
    name = input("Name: ")
    grade = int(input("Grade (e.g., 6-12): "))
    parent_number = input("Parent phone number (e.g., 859-555-1000): ")

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
    show_all_clubs()
    show_all_faculty()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub name: ")
    faculty_id = int(input("Faculty ID (e.g., 1): "))
    year = int(input("Year (YYYY): "))
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
    show_all_faculty()
    
    conn = get_connection()
    cursor = conn.cursor()
    faculty_id = int(input("\nFaculty ID (e.g., 1): "))
    year = int(input("Year (YYYY): "))
    sql = """
        SELECT club_name FROM Advises
        WHERE faculty_ID = %s AND year = %s
    """
    cursor.execute(sql, (faculty_id, year))
    print("\nClubs advised by faculty member:")
    for row in cursor:
        print(f"  • {row[0]}")
    print("\nNumber of rows:", cursor.rowcount)
    cursor.close()
    conn.close()

# get faculty ID by name
def get_faculty_id_by_name():
    show_all_faculty()
    
    conn = get_connection()
    cursor = conn.cursor()
    name = input("\nFaculty name: ").strip()
    sql = "SELECT faculty_ID FROM Faculty WHERE name = %s"
    cursor.execute(sql, (name,))
    results = cursor.fetchall()
    if results:
        print("Faculty ID(s):")
        for row in results:
            print(f"  • {row[0]}")
    else:
        print("Faculty member not found.")
    cursor.close()
    conn.close()

def view_faculty_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT faculty_ID, name, title, dept, phone_number, email FROM Faculty"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\n" + "="*110)
    print("FACULTY TABLE")
    print("="*110)
    print(f"{'ID':<5} {'Name':<25} {'Title':<15} {'Dept':<10} {'Phone':<15} {'Email':<30}")
    print("-"*110)
    
    if results:
        for row in results:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<15} {row[3]:<10} {row[4]:<15} {row[5]:<30}")
        print(f"\nTotal faculty members: {len(results)}")
    else:
        print("No faculty members found in the database.")
    
    print("="*110)
    
    cursor.close()
    conn.close()

def join_or_leave_club():
    show_all_clubs()
    show_all_students()
    
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("\nStudent ID (3-digit number, e.g., 101): "))
    year = int(input("Year (YYYY): "))
    
    # Show student's current clubs
    show_student_clubs(student_id, year)
    
    club_name = input("\nClub name: ")
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
    cursor.close()
    conn.close()
    
def list_club_members():
    show_all_clubs()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub name: ")
    year = int(input("Year (YYYY): "))
    sql = """
        SELECT s.name FROM Student s
        JOIN Member m ON s.student_ID = m.student_ID
        WHERE m.club_name = %s AND m.year = %s
    """
    cursor.execute(sql, (club_name, year))
    print("\nMembers:")
    for row in cursor:
        print(f"  • {row[0]}")
    cursor.close()
    conn.close()
    
def list_student_clubs():
    show_all_students()
    
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("\nStudent ID (3-digit number, e.g., 101): "))
    year = int(input("Year (YYYY): "))
    sql = "SELECT club_name FROM Member WHERE student_ID = %s AND year = %s"
    cursor.execute(sql, (student_id, year))
    print("\nClubs:")
    for row in cursor:
        print(f"  • {row[0]}")
    cursor.close()
    conn.close()
    
def student_schedule_on_date():
    show_all_students()
    
    conn = get_connection()
    cursor = conn.cursor()
    student_id = int(input("\nStudent ID (3-digit number, e.g., 101): "))
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
    cursor.close()
    conn.close()
    
def view_students_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT student_ID, name, grade, parent_number FROM Student"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\n" + "="*110)
    print("STUDENTS TABLE")
    print("="*110)
    print(f"{'ID':<10} {'Name':<25} {'Grade':<10} {'Parent Phone':<20}")
    print("-"*110)
    
    if results:
        for row in results:
            print(f"{row[0]:<10} {row[1]:<25} {row[2]:<10} {row[3]:<20}")
        print(f"\nTotal students: {len(results)}")
    else:
        print("No students found in the database.")
    
    print("="*110)
    
    cursor.close()
    conn.close()

def add_event():
    conn = get_connection()
    cursor = conn.cursor()
    
    event_id = int(input("Event ID (4-digit number, e.g., 1001): "))
    club_name = input("Club Name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM:SS): ")
    description = input("Description: ")
    event_type = input("Is this a Meeting (M) or Field Trip (F)? ").strip().upper()

    try:
        # REQUIREMENT 4b: Prevent overlapping meetings for the same club
        cursor.execute("""
            SELECT event_ID FROM Event 
            WHERE club_name = %s AND date = %s AND time = %s
        """, (club_name, date, time))
        
        if cursor.fetchone():
            print("\n Scheduling Conflict: This club already has an event scheduled at this date and time.")
            return  # Exit early to prevent the insert

        # Gather specific details depending on the event type
        if event_type == 'M':
            classroom = input("Classroom: ")
            
            # REQUIREMENT 4a: Prevent double-booking of classrooms
            cursor.execute("""
                SELECT e.event_ID 
                FROM Meeting m
                JOIN Event e ON m.event_ID = e.event_ID
                WHERE m.classroom = %s AND e.date = %s AND e.time = %s
            """, (classroom, date, time))
            
            if cursor.fetchone():
                print("\n Scheduling Conflict: This classroom is already booked at this date and time.")
                return  # Exit early to prevent the insert
                
        elif event_type == 'F':
            location = input("Location: ")
        else:
            print("\n Invalid event type. Please enter 'M' or 'F'.")
            return

        cursor.execute("""
            INSERT INTO Event (event_ID, club_name, date, time, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (event_id, club_name, date, time, description))
        
        # Insert into specific child table
        if event_type == 'M':
            cursor.execute("INSERT INTO Meeting (event_ID, classroom) VALUES (%s, %s)", (event_id, classroom))
        elif event_type == 'F':
            cursor.execute("INSERT INTO Field_Trip (event_ID, location) VALUES (%s, %s)", (event_id, location))
            
        conn.commit()
        print("\n Event added successfully.")
        
    except Exception as e:
        print(f"\nError adding event: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_event():
    show_all_events()
    
    conn = get_connection()
    cursor = conn.cursor()
    event_id = int(input("\nEnter Event ID to delete (4-digit number, e.g., 1001): "))
    
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
    show_all_clubs()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub Name: ")
    year = int(input("Year (YYYY): "))
    
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

def view_club_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT name FROM Club"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\n" + "="*70)
    print("CLUBS TABLE")
    print("="*70)
    print(f"{'Club Name':<15}")
    print("-"*70)
    
    if results:
        for row in results:
            print(f"{row[0]:<15}")
        print(f"\nTotal clubs: {len(results)}")
    else:
        print("No clubs found in the database.")
    
    print("="*70)
    
    cursor.close()
    conn.close()

def view_clubs_advisors():
    conn = get_connection()
    cursor = conn.cursor()
    year = int(input("Year (YYYY): "))
    
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

def view_club_events():
    show_all_clubs()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub Name: ")
    year = int(input("Year (YYYY): "))
    
    sql = """
        SELECT e.event_ID, e.date, e.time, e.description,
               IF(m.event_ID IS NOT NULL, 'Meeting', IF(ft.event_ID IS NOT NULL, 'Field Trip', 'Event')) as type
        FROM Event e
        LEFT JOIN Meeting m ON e.event_ID = m.event_ID
        LEFT JOIN Field_Trip ft ON e.event_ID = ft.event_ID
        WHERE e.club_name = %s AND YEAR(e.date) = %s
        ORDER BY e.date, e.time
    """
    cursor.execute(sql, (club_name, year))
    results = cursor.fetchall()
    
    print(f"\nEvents for {club_name} ({year}):")
    if results:
        for row in results:
            print(f"[{row[4]}] ID: {row[0]} | {row[1]} at {row[2]} | {row[3]}")
    else:
        print("No events found.")
        
    cursor.close()
    conn.close()

def record_budget():
    show_all_clubs()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub Name: ")
    year = int(input("Year (YYYY): "))
    total = float(input("Budget Total ($, e.g., 1500.00): "))
    
    try:
        cursor.execute("""
            INSERT INTO Budget (club_name, year, total) 
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE total = %s
        """, (club_name, year, total, total))
        conn.commit()
        print("Budget recorded successfully.")
    except Exception as e:
        print(f"Error recording budget: {e}")
    finally:
        cursor.close()
        conn.close()

def record_expense():
    show_budgets()
    
    conn = get_connection()
    cursor = conn.cursor()
    expense_id = int(input("\nExpense ID (e.g., 1): "))
    club_name = input("Club Name: ")
    year = int(input("Year (YYYY): "))
    amount = float(input("Amount ($, e.g., 200.00): "))
    memo = input("Memo: ")
    
    try:
        cursor.execute("""
            INSERT INTO Expense (expense_ID, club_name, year, amount, memo) 
            VALUES (%s, %s, %s, %s, %s)
        """, (expense_id, club_name, year, amount, memo))
        conn.commit()
        print("Expense recorded successfully.")
    except Exception as e:
        print(f"Error recording expense. Ensure a budget exists for this club and year. Error: {e}")
    finally:
        cursor.close()
        conn.close()

def report_club_finances():
    show_budgets()
    
    conn = get_connection()
    cursor = conn.cursor()
    club_name = input("\nClub Name: ")
    year = int(input("Year (YYYY): "))
    
    sql = """
        SELECT b.total, COALESCE(SUM(e.amount), 0)
        FROM Budget b
        LEFT JOIN Expense e ON b.club_name = e.club_name AND b.year = e.year
        WHERE b.club_name = %s AND b.year = %s
        GROUP BY b.total
    """
    cursor.execute(sql, (club_name, year))
    result = cursor.fetchone()
    
    if result:
        total_budget, total_expenses = result
        remaining = total_budget - total_expenses
        print(f"\nFinancial Report for {club_name} ({year}):")
        print(f"Total Budget:   ${total_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining:      ${remaining:.2f}")
    else:
        print("No budget found for this club and year.")
        
    cursor.close()
    conn.close()

def report_total_budgets():
    conn = get_connection()
    cursor = conn.cursor()
    year = int(input("Year (YYYY): "))
    
    cursor.execute("SELECT SUM(total) FROM Budget WHERE year = %s", (year,))
    result = cursor.fetchone()
    
    if result and result[0] is not None:
        print(f"\nTotal allocated budget for all clubs in {year}: ${result[0]:.2f}")
    else:
        print(f"No budgets recorded for {year}.")
        
    cursor.close()
    conn.close()

def main():
    print("\033c")
    launch()
    print("\033c")
    while True:
        print("\nClub Management System")
        print("1. Manage Clubs")
        print("2. Manage Faculty")
        print("3. Manage Students")
        print("4. Finances and Budgeting")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\033c")
            view_club_table()
            print("\n")
            print("\nClub Management")
            print("1. Add an event/meeting")
            print("2. Delete an event/meeting")
            print("3. View club events for a year")
            print("4. View club students for a year")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                add_event()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "2":
                delete_event()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "3":
                view_club_events()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "4":
                view_club_students()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "5":
                print("\033c")
                continue
        elif choice == "2":
            print("\033c")
            view_faculty_table()
            print("\n")
            print("\nFaculty Management")
            print("1. Get Faculty ID by Name")
            print("2. Assign a faculty advisor to a club")
            print("3. List all clubs advised by a faculty member")
            print("4. View all clubs and their advisors in a year")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                get_faculty_id_by_name()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "2":
                assign_advisor()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "3":
                list_advised_clubs()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "4":
                view_clubs_advisors()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "5":
                print("\033c")
                continue
        
        elif choice == "3":
            print("\033c")
            view_students_table()
            print("\n")
            print("\nStudent Management")
            print("1. Join or leave a club")
            print("2. List all members of a club")
            print("3. List all clubs a student belongs to")
            print("4. View student schedule on a date")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                join_or_leave_club()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "2":
                list_club_members()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "3":
                list_student_clubs()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "4":
                student_schedule_on_date()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "5":
                print("\033c")
                continue
        elif choice == "4":
            print("Finances and Budgeting")
            print("1. Record Budget")
            print("2. Record Expense")
            print("3. Report Club Finances")
            print("4. Report Total Budgets for a Year")
            print("5. Go Back")

            choice = input("Choose an option: ")
            if choice == "1":
                record_budget()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "2":
                record_expense()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "3":
                report_club_finances()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "4":
                report_total_budgets()
                print("Hit 'Enter' to continue...")
                input()
                print("\033c")
            elif choice == "5":
                print("\033c")
                continue
        elif choice == "5":
            print("Wiping credentials and exiting...")
            wipe_credentials()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
