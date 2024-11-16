import psycopg2
from psycopg2 import OperationalError
from admin_view import display_admin_menu, get_admin_choice
from lesson_controller import create_lesson

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
            location_name = input("Enter the location name: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            specialization = input("Enter the specialization (e.g., Yoga, Karate): ")
            
            # Collect the additional lesson details
            name = input("Enter the lesson name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            space_type = input("Enter the space type (e.g., Indoor, Outdoor): ")
            capacity = input("Enter the capacity: ")

            # Ensure capacity is an integer
            try:
                capacity = int(capacity)
            except ValueError:
                print("Invalid input for capacity. Please enter a number.")
                continue

            # Call the create_lesson function with user inputs
            create_lesson(name, address, city, space_type, capacity, location_name, date, specialization)

        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")
