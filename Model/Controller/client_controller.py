import psycopg2
from psycopg2 import OperationalError
from client_view import display_client_menu, get_client_choice

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

def handle_client_menu():
    while True:
        display_client_menu()
        choice = get_client_choice()

        if choice == "1":
            view_available_lessons()
        elif choice == "2":
            book_lesson()
        elif choice == "3":
            view_my_bookings()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def view_available_lessons():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT lesson_type_id, mode, start_date, end_date, location_id FROM lesson WHERE mode = true;")
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

def book_lesson():
    lesson_id = input("\nEnter the lesson ID to book: ")
    client_id = input("Enter your client ID: ")
    
    # Ensure lesson is available
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT availability FROM lessons WHERE lesson_id = %s;", (lesson_id,))
            lesson = cursor.fetchone()

            if lesson and lesson[0]:  # Check if the lesson is available
                # Insert the booking into the Bookings table
                cursor.execute("""
                    INSERT INTO bookings (client_id, lesson_id, booking_date)
                    VALUES (%s, %s, CURRENT_DATE) RETURNING booking_id;
                """, (client_id, lesson_id))
                booking_id = cursor.fetchone()[0]
                
                # Update lesson availability to false
                cursor.execute("""
                    UPDATE lessons
                    SET availability = false
                    WHERE lesson_id = %s;
                """, (lesson_id,))
                
                conn.commit()
                print(f"Booking successful! Your booking ID is {booking_id}.")
            else:
                print("This lesson is no longer available.")

        except Exception as e:
            print(f"Error booking lesson: {e}")
        finally:
            cursor.close()
            conn.close()

def view_my_bookings():
    client_id = input("\nEnter your client ID to view bookings: ")
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT b.booking_id, l.specialization, l.location, l.start_time, l.end_time 
                FROM bookings b
                JOIN lessons l ON b.lesson_id = l.lesson_id
                WHERE b.client_id = %s;
            """, (client_id,))
            bookings = cursor.fetchall()

            if not bookings:
                print("You have no bookings.")
            else:
                print("Your Bookings:")
                for booking in bookings:
                    print(f"Booking ID {booking[0]}: {booking[1]} at {booking[2]} - {booking[3]} to {booking[4]}")

        except Exception as e:
            print(f"Error fetching bookings: {e}")
        finally:
            cursor.close()
            conn.close()
