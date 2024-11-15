import psycopg2
from psycopg2 import sql, OperationalError

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "" #Make sure to put your own username
DB_PASSWORD = "" #Make sure to put your own password

def create_database():
    try:
        # Connect to PostgreSQL to create the new database
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            port="5432"
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
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(15) UNIQUE,
                age INTEGER,
                username VARCHAR(255),
                password VARCHAR(255)
            );"""

            create_instructor_table = """
            CREATE TABLE IF NOT EXISTS Instructor (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(15) UNIQUE,
                specialization VARCHAR(255),
                start_date DATE,
                end_date DATE
            );"""

            create_lesson_type_table = """
            CREATE TABLE IF NOT EXISTS LessonType (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) UNIQUE
            );"""

            create_space_type_table = """
            CREATE TABLE IF NOT EXISTS SpaceType (
                id SERIAL PRIMARY KEY,
                space_type VARCHAR(255) UNIQUE
            );"""

            create_location_table = """
            CREATE TABLE IF NOT EXISTS Location (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address TEXT,
                city VARCHAR(255),
                space_type VARCHAR(255),
                capacity INTEGER
            );"""

            create_schedule_table = """
            CREATE TABLE IF NOT EXISTS Schedule (
                id SERIAL PRIMARY KEY,
                start_date DATE,
                end_date DATE
            );"""

            create_offering_table = """
            CREATE TABLE IF NOT EXISTS Offering (
                id SERIAL PRIMARY KEY,
                isFull BOOLEAN,
                is_group_offering BOOLEAN,
                lesson_type_id INT,
                location_id INT,
                schedule_id INT,
                instructor_id INT,
                FOREIGN KEY (lesson_type_id) REFERENCES LessonType(id),
                FOREIGN KEY (location_id) REFERENCES Location(id),
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id),
                FOREIGN KEY (instructor_id) REFERENCES Instructor(id)
            );"""

            create_booking_table = """
            CREATE TABLE IF NOT EXISTS Booking (
                id SERIAL PRIMARY KEY,
                client_id INT,
                offering_id INT,
                FOREIGN KEY (client_id) REFERENCES Client(id),
                FOREIGN KEY (offering_id) REFERENCES Offering(id)
            );"""

            create_timeslot_table = """
            CREATE TABLE IF NOT EXISTS TimeSlot (
                id SERIAL PRIMARY KEY,
                schedule_id INT,
                start_time TIME,
                end_time TIME,
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id)
            );"""

            create_day_of_week_table = """
            CREATE TABLE IF NOT EXISTS DailySchedule (
                id SERIAL PRIMARY KEY,
                day_of_week VARCHAR(20)
            );"""

            # Execute table creation statements
            table_creation_queries = [
                create_client_table,
                create_instructor_table,
                create_lesson_type_table,
                create_space_type_table,
                create_location_table,
                create_schedule_table,
                create_offering_table,
                create_booking_table,
                create_timeslot_table,
                create_day_of_week_table
            ]

            for query in table_creation_queries:
                cursor.execute(query)

            print("Tables created successfully.")

            # DML Insert queries for all 10 tables

            # Insert Client data
            insert_client_data = """
            INSERT INTO Client (name, phone_number, age, username, password) 
            VALUES 
                ('John Doe', '1234567890', 25, 'john_doe', 'password123'),
                ('Jane Smith', '0987654321', 30, 'jane_smith', 'mypassword'),
                ('Alice Johnson', '1122334455', 22, 'alice_johnson', 'alice123'),
                ('Bob Martin', '2233445566', 35, 'bob_martin', 'bob2024'),
                ('Charlie Lee', '3344556677', 28, 'charlie_lee', 'charlie123'),
                ('Diana King', '4455667788', 40, 'diana_king', 'diana456'),
                ('Eva White', '5566778899', 26, 'eva_white', 'eva789'),
                ('Frank Blue', '6677889900', 33, 'frank_blue', 'frank321'),
                ('Grace Black', '7788990011', 29, 'grace_black', 'grace654'),
                ('Henry Grey', '8899001122', 45, 'henry_grey', 'henry987');
            """

            # Insert Instructor data
            insert_instructor_data = """
            INSERT INTO Instructor (name, phone_number, specialization, start_date, end_date)
            VALUES 
                ('Alice Brown', '5555555555', 'Yoga', '2024-01-01', '2024-12-31'),
                ('Bob White', '5555555556', 'Karate', '2024-01-15', '2024-06-30'),
                ('Catherine Red', '5555555557', 'Dance', '2024-02-01', '2024-12-31'),
                ('David Green', '5555555558', 'Swimming', '2024-03-01', '2024-09-30'),
                ('Emma Pink', '5555555559', 'Yoga', '2024-04-01', '2024-10-31'),
                ('Fiona Purple', '5555555560', 'Karate', '2024-05-01', '2024-12-31'),
                ('George Yellow', '5555555561', 'Dance', '2024-06-01', '2024-12-31'),
                ('Helen Brown', '5555555562', 'Swimming', '2024-07-01', '2024-12-31'),
                ('Ian Blue', '5555555563', 'Yoga', '2024-08-01', '2024-12-31'),
                ('Jack Orange', '5555555564', 'Karate', '2024-09-01', '2024-12-31');
            """

            # Insert LessonType data
            insert_lesson_type_data = """
            INSERT INTO LessonType (name) 
            VALUES 
                ('Yoga'),
                ('Karate'),
                ('Dance'),
                ('Swimming');
            """

            # Insert Location data
            insert_location_data = """
            INSERT INTO Location (name, address, city, space_type, capacity)
            VALUES 
                ('Pool', '123 Pool St', 'Toronto', 'Pool', 30),
                ('Gym', '456 Gym Rd', 'Waterloo', 'Gym', 50),
                ('Studio', '789 Studio Blvd', 'Vancouver', 'Studio', 40),
                ('Pool', '101 Pool St', 'Ottawa', 'Pool', 35),
                ('Gym', '202 Gym Rd', 'Calgary', 'Gym', 60),
                ('Studio', '303 Studio Ave', 'Montreal', 'Studio', 45),
                ('Pool', '404 Pool St', 'Toronto', 'Pool', 25),
                ('Gym', '505 Gym Rd', 'Vancouver', 'Gym', 70),
                ('Studio', '606 Studio Blvd', 'Waterloo', 'Studio', 50),
                ('Pool', '707 Pool St', 'Calgary', 'Pool', 30);
            """

            # Insert Schedule data
            insert_schedule_data = """
            INSERT INTO Schedule (start_date, end_date)
            VALUES 
                ('2024-01-01', '2024-01-31'),
                ('2024-02-01', '2024-02-28'),
                ('2024-03-01', '2024-03-31'),
                ('2024-04-01', '2024-04-30'),
                ('2024-05-01', '2024-05-31'),
                ('2024-06-01', '2024-06-30'),
                ('2024-07-01', '2024-07-31'),
                ('2024-08-01', '2024-08-31'),
                ('2024-09-01', '2024-09-30'),
                ('2024-10-01', '2024-10-31');
            """

            # Insert Offering data
            insert_offering_data = """
            INSERT INTO Offering (isFull, is_group_offering, lesson_type_id, location_id, schedule_id, instructor_id)
            VALUES 
                (FALSE, TRUE, 1, 1, 1, 1),
                (TRUE, FALSE, 2, 2, 2, 2),
                (FALSE, TRUE, 3, 3, 3, 3),
                (TRUE, FALSE, 4, 4, 4, 4),
                (FALSE, TRUE, 1, 5, 5, 5),
                (TRUE, FALSE, 2, 6, 6, 6),
                (FALSE, TRUE, 3, 7, 7, 7),
                (TRUE, FALSE, 4, 8, 8, 8),
                (FALSE, TRUE, 1, 9, 9, 9),
                (TRUE, FALSE, 2, 10, 10, 10);
            """

            # Insert Booking data
            insert_booking_data = """
            INSERT INTO Booking (client_id, offering_id) 
            VALUES 
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
                (10, 10);
            """

            # Insert TimeSlot data
            insert_timeslot_data = """
            INSERT INTO TimeSlot (schedule_id, start_time, end_time) 
            VALUES 
                (1, '09:00', '10:00'),
                (2, '10:00', '11:00'),
                (3, '11:00', '12:00'),
                (4, '12:00', '13:00'),
                (5, '13:00', '14:00'),
                (6, '14:00', '15:00'),
                (7, '15:00', '16:00'),
                (8, '16:00', '17:00'),
                (9, '17:00', '18:00'),
                (10, '18:00', '19:00');
            """

            # Insert DailySchedule data
            insert_daily_schedule_data = """
            INSERT INTO DailySchedule (day_of_week) 
            VALUES 
                ('Monday'),
                ('Tuesday'),
                ('Wednesday'),
                ('Thursday'),
                ('Friday'),
                ('Saturday'),
                ('Sunday');
            """

            # Execute all insert statements
            cursor.execute(insert_client_data)
            cursor.execute(insert_instructor_data)
            cursor.execute(insert_lesson_type_data)
            cursor.execute(insert_location_data)
            cursor.execute(insert_schedule_data)
            cursor.execute(insert_offering_data)
            cursor.execute(insert_booking_data)
            cursor.execute(insert_timeslot_data)
            cursor.execute(insert_daily_schedule_data)

            print("Data inserted successfully.")
except OperationalError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
