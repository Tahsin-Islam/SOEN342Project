import psycopg2
from psycopg2 import OperationalError
from admin_view import display_admin_menu, get_admin_choice
from lesson_controller import create_lesson
from cancelbooking import get_user_bookings, delete_booking

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

def handle_admin_menu():
    while True:
        display_admin_menu()  # Show the admin menu
        choice = get_admin_choice()  # Get the admin's choice

        if choice == "1":
            # Collect parameters for creating a lesson
            create_lesson()        
        elif choice == "2":
            client_id = input("Enter the client ID to view bookings: ")
            try:
                # Ensure client_id is an integer
                client_id = int(client_id)
            except ValueError:
                print("Invalid client ID. Please enter a number.")
                continue

            # Display the user's bookings
            bookings = get_user_bookings(client_id)

            if bookings:
                # Ask if they want to delete a booking
                delete_choice = input("Do you want to delete a booking? (yes/no): ").strip().lower()
                if delete_choice == "yes":
                    try:
                        offering_id_to_delete = input("Enter the Offering ID to delete: ")
                        # Ensure offering_id is an integer
                        offering_id_to_delete = int(offering_id_to_delete)
                        delete_booking(client_id, offering_id_to_delete)
                    except ValueError:
                        print("Invalid Offering ID. Please enter a number.")
                else:
                    print("No bookings were deleted.")
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")
