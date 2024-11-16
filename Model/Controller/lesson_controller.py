import psycopg2
from psycopg2 import OperationalError

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tahsinislam"  # Replace with your own username
DB_PASSWORD = ""  # Replace with your own password

def get_user_choice(options, prompt_message):
    """
    Utility function to display options and get user selection.
    """
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    while True:
        try:
            choice = int(input(prompt_message))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_lesson():
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as connection:
            with connection.cursor() as cursor:
                # Prompt user for lesson type
                lesson_type = input("Enter the lesson type (e.g., Yoga, Karate, etc.): ").strip()

                # Fetch lesson type ID
                cursor.execute("SELECT id FROM LessonType WHERE name = %s", (lesson_type,))
                result = cursor.fetchone()
                if not result:
                    print(f"Lesson type '{lesson_type}' not found. Please ensure it exists in the database.")
                    return
                lesson_type_id = result[0]

                # Fetch locations
                cursor.execute("SELECT id, name FROM Location")
                locations = cursor.fetchall()
                if not locations:
                    print("No locations available.")
                    return

                print("\nAvailable Locations:")
                location_choice = get_user_choice(
                    [f"{loc[1]} (ID: {loc[0]})" for loc in locations],
                    "Select a location by number: "
                )
                location_id = locations[location_choice - 1][0]

                # Fetch available timeslots for the selected location
                cursor.execute("""
                    SELECT DISTINCT ON (ts.id) 
                        ts.id AS timeslot_id, 
                        ts.start_time, 
                        ts.end_time, 
                        ds.day_of_week, 
                        sch.start_date, 
                        sch.end_date
                    FROM Location loc
                    JOIN Schedule sch ON loc.schedule_id = sch.id
                    JOIN schedule_dailySchedule ssch ON sch.id = ssch.schedule_id
                    JOIN DailySchedule ds ON ds.id = ssch.daily_schedule_id
                    JOIN DailyScheduleTimeSlot dsts ON dsts.daily_schedule_id = ds.id
                    JOIN TimeSlot ts ON ts.id = dsts.timeslot_id
                    WHERE loc.id = %s
                """, (location_id,))

                timeslots = cursor.fetchall()
                if not timeslots:
                    print("No available timeslots for the selected location.")
                    return

                print("\nAvailable Timeslots:")
                timeslot_choice = get_user_choice(
                    [
                        f"Time Slot ID: {t[0]}, Start: {t[1]}, End: {t[2]}, Day: {t[3]}, "
                        f"Schedule Start Date: {t[4]}, Schedule End Date: {t[5]}"
                        for t in timeslots
                    ],
                    "Select a timeslot by number: "
                )
                timeslot_id = timeslots[timeslot_choice - 1][0]

                # Get additional lesson details
                mode = input("Is the lesson online? (yes/no): ").strip().lower() == "yes"
                start_date = input("Enter the lesson start date (YYYY-MM-DD): ").strip()
                end_date = input("Enter the lesson end date (YYYY-MM-DD): ").strip()

                # Insert the new lesson
                cursor.execute("""
                    INSERT INTO Lesson (lesson_type_id, mode, start_date, end_date, location_id, timeslot_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (lesson_type_id, mode, start_date, end_date, location_id, timeslot_id))
                connection.commit()

                print("New lesson created successfully.")

    except OperationalError as e:
        print(f"Database connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

