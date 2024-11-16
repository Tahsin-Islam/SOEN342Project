import psycopg2
from psycopg2 import sql, OperationalError

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"  # Make sure to put your own username
DB_PASSWORD = ""  # Make sure to put your own password

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
    # Connect to the newly created database
    with psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
    ) as connection:
        with connection.cursor() as cursor:
            print("Connected to PostgreSQL database")

            # Create tables
            create_client_table = """
            CREATE TABLE IF NOT EXISTS Client (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(15) UNIQUE,
                age INTEGER,
                username VARCHAR(255),
                password VARCHAR(255)
            );
            """

            create_instructor_table = """
            CREATE TABLE IF NOT EXISTS Instructor (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(15) UNIQUE,
                specialization VARCHAR(255),
                start_date DATE,
                end_date DATE
            );
            """

            create_instructor_availability_table = """
            CREATE TABLE IF NOT EXISTS Instructor_Availability (
                instructor_id INT,
                city TEXT,
                PRIMARY KEY (instructor_id, city),
                FOREIGN KEY (instructor_id) REFERENCES Instructor(id)
            );
            """

            create_lesson_type_table = """
            CREATE TABLE IF NOT EXISTS LessonType (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) UNIQUE
            );
            """

            create_schedule_table = """
            CREATE TABLE IF NOT EXISTS Schedule (
                id SERIAL PRIMARY KEY,
                start_date DATE,
                end_date DATE
            );
            """

            create_location_table = """
            CREATE TABLE IF NOT EXISTS Location (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address TEXT,
                city VARCHAR(255),
                space_type VARCHAR(255),
                capacity INTEGER,
                schedule_id INTEGER,
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id) ON DELETE SET NULL
            );
            """

            create_lesson_table = """
            CREATE TABLE IF NOT EXISTS Lesson (
                id SERIAL PRIMARY KEY,
                lesson_type_id INT,
                mode BOOLEAN,
                start_date DATE,
                end_date DATE,
                location_id INT,
                FOREIGN KEY (lesson_type_id) REFERENCES LessonType(id),
                FOREIGN KEY (location_id) REFERENCES Location(id)
            );
            """

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
            );
            """

            create_timeslot_table = """
            CREATE TABLE IF NOT EXISTS TimeSlot (
                id SERIAL PRIMARY KEY,
                start_time TIME,
                end_time TIME
            );
            """

            create_daily_schedule_table = """
            CREATE TABLE IF NOT EXISTS DailySchedule (
                id SERIAL PRIMARY KEY,
                day_of_week VARCHAR(20)
            );
            """

            create_lesson_time_slots_table = """
            CREATE TABLE IF NOT EXISTS LessonTimeSlot (
                lesson_id INT,
                timeslot_id INT,
                PRIMARY KEY (lesson_id, timeslot_id),
                FOREIGN KEY (lesson_id) REFERENCES Lesson(id) ON DELETE CASCADE,
                FOREIGN KEY (timeslot_id) REFERENCES TimeSlot(id) ON DELETE CASCADE
            );
            """

            create_daily_schedule_timeslot_table = """
            CREATE TABLE IF NOT EXISTS DailyScheduleTimeSlot (
                id SERIAL PRIMARY KEY,
                daily_schedule_id INT NOT NULL,
                timeslot_id INT NOT NULL,
                FOREIGN KEY (daily_schedule_id) REFERENCES DailySchedule(id),
                FOREIGN KEY (timeslot_id) REFERENCES TimeSlot(id)
            );
            """
            create_sch_daily_sch_table ="""
                CREATE TABLE IF NOT EXISTS ScheduleDailySchedule (
                schedule_id INT,
                daily_schedule_id INT,
                PRIMARY KEY (schedule_id, daily_schedule_id) ,
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id) ON DELETE CASCADE,
                FOREIGN KEY (daily_schedule_id) REFERENCES DailySchedule(id) ON DELETE CASCADE
            );
            """
            create_booking_table = """
                CREATE TABLE IF NOT EXISTS booking(
                    offering_id INT REFERENCES Offering(id) ON DELETE CASCADE,
                    client_id INT REFERENCES Client(id)ON DELETE CASCADE
            )
            """

            # Execute table creation queries
            table_creation_queries = [
                create_client_table,
                create_instructor_table,
                create_instructor_availability_table,
                create_lesson_type_table,
                create_schedule_table,
                create_location_table,
                create_lesson_table,
                create_offering_table,
                create_timeslot_table,
                create_daily_schedule_table,
                create_lesson_time_slots_table,
                create_daily_schedule_timeslot_table,
                create_sch_daily_sch_table,
                create_booking_table,
            ]

            for query in table_creation_queries:
                cursor.execute(query)

            print("Tables created successfully.")

            insert_queries = [
                # Insert Client data
                ("INSERT INTO Client (name, phone_number, age, username, password) VALUES (%s, %s, %s, %s, %s);", [
                    ('John Doe', '1234567890', 30, 'john_doe', 'password123'),
                    ('Jane Smith', '9876543210', 28, 'jane_smith', 'password456'),
                    ('Charlie Brown', '5559876543', 35, 'charlie_brown', 'password789'),
                    ('Emily White', '5556543210', 40, 'emily_white', 'password101'),
                    ('David Green', '5551239876', 25, 'david_green', 'password202')
                ]),

                # Insert Instructor data
                ("INSERT INTO Instructor (name, phone_number, specialization, start_date, end_date) VALUES (%s, %s, %s, %s, %s);", [
                    ('Alice Johnson', '5551234567', 'Yoga', '2024-01-01', '2024-12-31'),
                    ('Bob Brown', '5552345678', 'Karate', '2024-03-01', '2024-09-30'),
                    ('Catherine Lee', '5553456789', 'Pilates', '2024-04-01', '2024-10-30'),
                    ('Daniel Kim', '5554567890', 'Boxing', '2024-02-01', '2024-08-31'),
                    ('Ella Wilson', '5555678901', 'Swimming', '2024-05-01', '2024-11-30')
                ]),

                # Insert LessonType data
                ("INSERT INTO LessonType (name) VALUES (%s);", [
                    ('Yoga',),
                    ('Karate',),
                    ('Pilates',),
                    ('Boxing',),
                    ('Swimming',)
                ]),

                # Insert Schedule data
                ("INSERT INTO Schedule (start_date, end_date) VALUES (%s, %s);", [
                    ('2024-01-01', '2024-12-31'),
                    ('2024-02-01', '2024-07-31'),
                    ('2024-03-01', '2024-09-30'),
                    ('2024-04-01', '2024-10-31')
                ]),

                # Insert Location data
                ("INSERT INTO Location (name, address, city, space_type, capacity, schedule_id) VALUES (%s, %s, %s, %s, %s, %s);", [
                    ('Downtown Studio', '123 Main St', 'Toronto', 'Indoor', 50, 1),
                    ('Uptown Gym', '456 Elm St', 'Toronto', 'Outdoor', 30, 2),
                    ('City Park', '789 Oak St', 'Toronto', 'Outdoor', 100, 3),
                    ('Beachfront Center', '101 Lake Ave', 'Toronto', 'Indoor', 70, 4)
                ]),

                # Insert Offering data
                ("INSERT INTO Offering (isFull, is_group_offering, lesson_type_id, location_id, schedule_id, instructor_id) VALUES (%s, %s, %s, %s, %s, %s);", [
                    (False, True, 1, 1, 1, 1),  # Yoga at Downtown Studio
                    (False, False, 2, 2, 2, 2),  # Karate at Uptown Gym
                    (True, True, 3, 3, 3, 3),    # Pilates at City Park
                    (False, False, 4, 4, 4, 4)   # Swimming at Beachfront Center
                ]),

                # Insert TimeSlot data
                ("INSERT INTO TimeSlot (start_time, end_time) VALUES (%s, %s);", [
                    ('08:00', '09:00'),
                    ('09:00', '10:00'),
                    ('10:00', '11:00'),
                    ('11:00', '12:00')
                ]),

                # Insert DailySchedule data
                ("INSERT INTO DailySchedule (day_of_week) VALUES (%s);", [
                    ('Monday',),
                    ('Wednesday',),
                    ('Friday',),
                    ('Sunday',)
                ]),

                # Insert Lesson data
                ("INSERT INTO Lesson (lesson_type_id, mode, start_date, end_date, location_id) VALUES (%s, %s, %s, %s, %s);", [
                    (1, True, '2024-01-01', '2024-12-31', 1),  # Yoga at Downtown Studio
                    (2, False, '2024-02-01', '2024-07-31', 2),  # Karate at Uptown Gym
                    (3, True, '2024-03-01', '2024-09-30', 3),    # Pilates at City Park
                    (4, False, '2024-04-01', '2024-10-31', 4)    # Swimming at Beachfront Center
                ]),

                # Insert LessonTimeSlot data
                ("INSERT INTO LessonTimeSlot (lesson_id, timeslot_id) VALUES (%s, %s);", [
                    (1, 1),  # Yoga at Downtown Studio
                    (2, 2),  # Karate at Uptown Gym
                    (3, 3),  # Pilates at City Park
                    (4, 4)   # Swimming at Beachfront Center
                ]),

                # Insert DailyScheduleTimeSlot data
                ("INSERT INTO DailyScheduleTimeSlot (daily_schedule_id, timeslot_id) VALUES (%s, %s);", [
                    (1, 1),  # Monday with first timeslot
                    (2, 2),  # Wednesday with second timeslot
                    (3, 3),  # Friday with third timeslot
                    (4, 4)   # Sunday with fourth timeslot
                ]),
                
                ("INSERT INTO ScheduleDailySchedule (daily_schedule_id, schedule_id) VALUES (%s, %s);", [
                    (1, 1),  # Monday with first timeslot
                    (2, 2),  # Wednesday with second timeslot
                    (3, 3),  # Friday with third timeslot
                    (4, 4)   # Sunday with fourth timeslot
                ])
            ]

            # Execute insert queries
            for query, data in insert_queries:
                cursor.executemany(query, data)

            print("Data inserted successfully.")


except OperationalError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")