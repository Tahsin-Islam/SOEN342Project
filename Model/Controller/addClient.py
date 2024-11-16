import psycopg2
from psycopg2 import OperationalError

# Database configuration (replace with actual credentials)
DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"
DB_PASSWORD = "your_password"

def add_client_to_database(name, phone_number, age):
    """Adds a new client to the Client table."""
    insert_query = """
    INSERT INTO Client (name, phone_number, age)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    try:
        # Connect to the database
        with psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        ) as connection:
            with connection.cursor() as cursor:
                # Execute the insert query
                cursor.execute(insert_query, (name, phone_number, age))
                connection.commit()  # Commit the transaction
                client_id = cursor.fetchone()[0]
                print(f"Client added successfully with ID: {client_id}")
                return client_id  # Return the client ID for further use if needed
    except Exception as e:
        print("Error adding the client:", e)
