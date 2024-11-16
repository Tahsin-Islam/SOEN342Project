import psycopg2
from psycopg2 import sql

# Database connection settings
DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"  # Change to your database user
DB_PASSWORD = ""  # Change to your database password

# Function to get the user's bookings
def get_user_bookings(client_id):
    try:
        # Connect to the database
        with psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        ) as connection:
            with connection.cursor() as cursor:
                # SQL query to get bookings for the specific client
                query = """
                SELECT *
                FROM booking b
                JOIN Offering o ON b.offering_id = o.id
                JOIN Lesson l ON o.lesson_type_id = l.lesson_type_id
                WHERE b.client_id = %s;
                """
                cursor.execute(query, (client_id,))
                bookings = cursor.fetchall()

                if not bookings:
                    print("No bookings found for this client.")
                else:
                    for booking in bookings:
                        print(f"Offering ID: {booking[0]}, Lesson: {booking[3]}, Start Date: {booking[4]}, End Date: {booking[5]}, Location: {booking[6]}")
                return bookings
    except Exception as e:
        print(f"Error retrieving bookings: {e}")

# Function to delete a booking by offering_id
def delete_booking(client_id, offering_id):
    try:
        # Connect to the database
        with psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        ) as connection:
            with connection.cursor() as cursor:
                # SQL query to delete the booking
                query = """
                DELETE FROM booking
                WHERE client_id = %s AND offering_id = %s;
                """
                cursor.execute(query, (client_id, offering_id))
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"Booking with Offering ID {offering_id} deleted successfully.")
                else:
                    print("No such booking found for this client.")
    except Exception as e:
        print(f"Error deleting booking: {e}")

# Example usage:
# Step 1: Get the bookings for the client with ID 1
client_id = 1
bookings = get_user_bookings(client_id)

# Step 2: Delete a specific booking by offering_id (e.g., offering_id 3)
if bookings:
    offering_id_to_delete = bookings[0][0]  # Let's assume we want to delete the first booking
    delete_booking(client_id, offering_id_to_delete)
