import psycopg2
from psycopg2 import OperationalError
from instructor_view import display_instructor_menu, get_instructor_choice

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"  # Replace with your own username
DB_PASSWORD = ""  # Replace with your own password

def get_db_connection():
    """Utility function to get a database connection."""
    try:
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None
    
def handle_instructor_menu():
    while True:
        display_instructor_menu()  # Show the admin menu
        choice = get_instructor_choice()  # Get the admin's choice

        if choice == "1":
            select_available_lessons()
        elif choice == "2":
            print("Logging out...")
            break

def select_available_lessons():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT lesson_type_id, mode, start_date, end_date, location_id FROM lesson;")
            lessons = cursor.fetchall()

            if not lessons:
                print("No available lessons found.")
            else:
                print("Available Lessons:")
                for lesson in lessons:
                    print(f"{lesson[0]}. {lesson[1]} at {lesson[2]} - {lesson[3]} to {lesson[4]}")

        except Exception as e:
            print(f"Error fetching lessons: {e}")
        finally:
            cursor.close()
            conn.close()