import psycopg2
from psycopg2 import sql

DB_HOST = "localhost"
DB_NAME = "lesson_management_system"
DB_USER = "tank"
DB_PASSWORD = ""

def manage_user_lessons(user_id):
    try:
        with psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as connection:
            with connection.cursor() as cursor:
                # Fetch the user's related time slots, daily schedule, and lessons
                fetch_query = """
                SELECT 
                    l.id AS lesson_id,
                    lt.name AS lesson_type,
                    l.mode AS online,
                    ds.day_of_week,
                    ts.start_time,
                    ts.end_time,
                    loc.name AS location_name,
                    loc.address AS location_address,
                    o.isFull AS availability
                FROM Lesson l
                INNER JOIN LessonType lt ON l.lesson_type_id = lt.id
                INNER JOIN Location loc ON l.location_id = loc.id
                INNER JOIN LessonTimeSlot lts ON l.id = lts.lesson_id
                INNER JOIN TimeSlot ts ON lts.timeslot_id = ts.id
                INNER JOIN Schedule s ON loc.schedule_id = s.id
                INNER JOIN ScheduleDailySchedule sds ON s.id = sds.schedule_id
                INNER JOIN DailySchedule ds ON sds.daily_schedule_id = ds.id
                INNER JOIN Offering o ON l.lesson_type_id = o.lesson_type_id
                WHERE o.isFull = FALSE; -- Only fetch available lessons
                """
                cursor.execute(fetch_query)
                lessons = cursor.fetchall()

                print("Available lessons and time slots:")
                for idx, lesson in enumerate(lessons, start=1):
                    print(
                        f"{idx}. Lesson ID: {lesson[0]}, Type: {lesson[1]}, Online: {'Yes' if lesson[2] else 'No'}, "
                        f"Day: {lesson[3]}, Time: {lesson[4]} - {lesson[5]}, "
                        f"Location: {lesson[6]}, Address: {lesson[7]}, Availability: {'Available' if not lesson[8] else 'Full'}"
                    )

                # User selects a lesson
                lesson_choice = int(input("Select a lesson number to enroll (e.g., 1, 2, 3): ")) - 1
                selected_lesson = lessons[lesson_choice]
                selected_lesson_id = selected_lesson[0]

                # Update the availability of the selected lesson
                update_query = """
                UPDATE Offering
                SET isFull = TRUE
                WHERE lesson_type_id = (
                    SELECT lesson_type_id FROM Lesson WHERE id = %s
                );
                """
                cursor.execute(update_query, (selected_lesson_id,))
                print(f"Lesson {selected_lesson_id} set to unavailable.")

                # Create a new offering for the same lesson type
                new_offering_query = """
                INSERT INTO Offering (isFull, is_group_offering, lesson_type_id, location_id, schedule_id, instructor_id)
                SELECT FALSE, FALSE, lesson_type_id, location_id, schedule_id, instructor_id
                FROM Offering
                WHERE lesson_type_id = (
                    SELECT lesson_type_id FROM Lesson WHERE id = %s
                )
                LIMIT 1
                RETURNING id;
                """
                cursor.execute(new_offering_query, (selected_lesson_id,))
                new_offering_id = cursor.fetchone()[0]
                print(f"New offering created with ID: {new_offering_id}")

                connection.commit()
                print("Transaction completed successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

manage_user_lessons(1)
