### Operation:
`offerNewLesson(lessonType, mode);` 

### Cross References:
Use case - Process Bookings
### Preconditions:
- The `Admin` must be logged into the system
- The various `lessonType` must be predefined
- The location for the lesson must exist in the Location database
- The `Instructor` must be qualified to teach the `Lesson`
### Postconditions:
- If the lesson being requested to create does not exist within the Lesson database:
  - A new `Lesson` will be created using attributes such as: `lessonType`, `mode`, `address`, `city`
  - The `Admin` will receive a confirmation message saying that the lesson was created
- If the `Lesson` being requested to create exists within the Lesson database:
  - The lesson will not be created
  - A message will return to the admin saying that the lesson already exists and was not created

