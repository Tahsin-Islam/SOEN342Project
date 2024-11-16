import psycopg2
from psycopg2 import sql, OperationalError

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"  # Make sure to put your own username
DB_PASSWORD = ""  # Make sure to put your own password

def get_available_offerings():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        with connection.cursor() as cursor:
            # Query to get all offerings that are not full
            cursor.execute("""
                SELECT o.id, lt.name AS lesson_type, l.name AS location, i.name AS instructor
                FROM Offering o
                JOIN LessonType lt ON o.lesson_type_id = lt.id
                JOIN Location l ON o.location_id = l.id
                JOIN Instructor i ON o.instructor_id = i.id
                WHERE o.isFull = FALSE;
            """)

            offerings = cursor.fetchall()

            if offerings:
                print("Available Offerings:")
                for index, offering in enumerate(offerings, 1):
                    print(f"{index}. {offering[1]} at {offering[2]} with {offering[3]}")

                # Ask the user to select an offering
                selection = int(input("Please select an offering by number: "))
                if 1 <= selection <= len(offerings):
                    # Return the ID of the selected offering
                    selected_offering_id = offerings[selection-1][0]
                    return selected_offering_id
                else:
                    print("Invalid selection.")
                    return None
            else:
                print("No available offerings.")
                return None

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection:
            connection.close()


def create_booking(client_id, offering_id):
    if offering_id is None:
        print("No valid offering ID provided.")
        return

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        with connection.cursor() as cursor:
            # Insert a booking for the client and offering
            cursor.execute("""
                INSERT INTO booking (client_id, offering_id) 
                VALUES (%s, %s);
            """, (client_id, offering_id))

            # Update the offering to mark it as full
            cursor.execute("""
                UPDATE Offering 
                SET isFull = TRUE 
                WHERE id = %s;
            """, (offering_id,))

            # Commit the transaction
            connection.commit()

            print(f"Booking created successfully for offering {offering_id}.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

# Example Usage
client_id = 1  # Assume client is logged in with id 1



# If offerings are returned as None (meaning an error or no offerings), avoid trying to book
def book_offer(user_id):
    x = get_available_offerings()

    if x is not None:
        create_booking(user_id, x)
    else:
        print("No available offerings to book.")

