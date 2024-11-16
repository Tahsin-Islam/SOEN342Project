import psycopg2
from psycopg2 import OperationalError
from client_view import display_client_menu, get_client_choice
from selectlesson import manage_user_lessons
from bookoffering import book_offer
from cancelbooking import get_user_bookings, delete_booking
from addClient import add_client_to_database

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
            book_lesson()
        elif choice == "2":
            age = input("Enter your age: ")
            try:
                age = int(age)
                if age < 18:
                    print("You must be 18 or older to create a booking. Returning to the menu.")
                    continue  # Return to the menu if not old enough
            except ValueError:
                print("Invalid age. Please enter a numeric value.")
                continue

            # If age verification passes, proceed with booking
            client_id = input("\nEnter your client ID: ")
            try:
                user_id = int(client_id)  # Ensure the input is valid
                book_offer(user_id)  # Pass the validated user ID to the booking function
            except ValueError:
                print("Invalid client ID. Please enter a numeric value.")

        elif choice == "3":
            view_my_bookings()
        elif choice == "4":
            client_id = input("\nEnter your client ID: ")
            try:
                user_id = int(client_id)  # Ensure the input is valid
                manage_user_lessons(user_id)
            except ValueError:
                print("Invalid client ID. Please enter a numeric value.")
        elif choice == "5":
            client_id = input("\nEnter your Client ID: ")
            try:
                user_id = int(client_id)
                get_user_bookings(client_id)
                offering_id = input("\nEnter offering ID: ")
                delete_booking(user_id, offering_id)
            except ValueError:
                print("Invalid Client ID")
        elif choice == "6":
            print("\nAdd a New Client")
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            age = input("Enter your age: ")
            try:
                age = int(age)  # Validate age as an integer
                if age < 0:
                    print("Age cannot be negative.")
                else:
                    # Call the function to add the client to the database
                    add_client_to_database(name, phone_number, age)
            except ValueError:
                print("Invalid age. Please enter a numeric value.")

        elif choice == "7":
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
            cursor.execute("SELECT * FROM offering WHERE id = %s;", (lesson_id,))
            lesson = cursor.fetchone()

            if lesson and lesson[0]:  # Check if the lesson is available
                # Insert the booking into the Bookings table
                cursor.execute("""
                    INSERT INTO booking (client_id, offering_id)
                    VALUES (%s, %s) RETURNING id;
                """, (client_id, lesson_id))
                booking_id = cursor.fetchone()[0]
                
                # Update lesson availability to false
                cursor.execute("""
                    UPDATE offering
                    SET isFull = false
                    WHERE id = %s;
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
                SELECT b.id, l.address
                FROM booking b
                JOIN offering o ON b.offering_id = o.id
                JOIN location l ON l.id = o.location_id
                WHERE b.client_id = %s;
            """, (client_id,))
            bookings = cursor.fetchall()

            if not bookings:
                print("You have no bookings.")
            else:
                print("Your Bookings:")
                for booking in bookings:
                    print(f"Booking ID {booking[0]}: {booking[1]}")

        except Exception as e:
            print(f"Error fetching bookings: {e}")
        finally:
            cursor.close()
            conn.close()
