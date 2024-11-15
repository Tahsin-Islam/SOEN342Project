import requests
import psycopg2
from psycopg2 import sql, OperationalError

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = ""
DB_PASSWORD = ""

def create_database():
    try:
        # Connect to PostgreSQL to create the new database
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        connection.autocommit = True
        cursor = connection.cursor()
        
        new_db_name = "lesson_management_system"
        
        create_db_query = sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(new_db_name)
        )

        try:
            cursor.execute(create_db_query)
            print(f"Database '{new_db_name}' created successfully.")
        except psycopg2.errors.DuplicateDatabase:
            print(f"Database '{new_db_name}' already exists.")
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            cursor.close()
            connection.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")

create_database()

try:
    with psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
    ) as connection:
        with connection.cursor() as cursor:
            print("Connected to PostgreSQL database")

            create_client_table = """
            CREATE TABLE IF NOT EXISTS Client (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT UNIQUE,
                age INTEGER,
                username VARCHAR(255),
                password VARCHAR(255)
            );"""

            create_instructor_table = """
            CREATE TABLE IF NOT EXISTS Instructor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT UNIQUE,
                specialization TEXT,
                start_date TEXT,
                end_date TEXT
            );"""

            create_lesson_type_table = """
            CREATE TABLE IF NOT EXISTS LessonType (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            );"""

            create_space_type_table = """
            CREATE TABLE IF NOT EXISTS SpaceType (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                space_type TEXT UNIQUE
            );"""

            create_location_table = """
            CREATE TABLE IF NOT EXISTS Location (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                city TEXT,
                space_type TEXT,
                capacity INTEGER
            );"""

            create_schedule_table = """
            CREATE TABLE IF NOT EXISTS Schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_date TEXT,
                end_date TEXT
            );"""

            create_offering_table = """
            CREATE TABLE IF NOT EXISTS Offering (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full BOOLEAN,
                isGroupOffering BOOLEAN,
                lessonType TEXT UNIQUE,
                location_id INT,
                schedule_id INT,
                instructor_id INT,
                FOREIGN KEY (location_id) REFERENCES Location(id),
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id),
                FOREIGN KEY (instructor_id) REFERENCES Instructor(id)
            );"""

            create_booking_table = """
            CREATE TABLE IF NOT EXISTS Booking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INT,
                offering_id INT,
                FOREIGN KEY (client_id) REFERENCES Client(id),
                FOREIGN KEY (offering_id) REFERENCES Offering(bookingNumber)
            );"""

            create_timeslot_table = """
            CREATE TABLE TimeSlot (
                id INT PRIMARY KEY AUTO_INCREMENT,
                schedule_id INT,
                start_time TIME,
                end_time TIME,
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id)
            );"""

            create_day_of_week_table = """
            CREATE TABLE DailySchedule (
                id INT PRIMARY KEY AUTO_INCREMENT,
                day_of_week VARCHAR(20)
            );"""
        print("Tables created successfully.")
except OperationalError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error occurred: {e}")