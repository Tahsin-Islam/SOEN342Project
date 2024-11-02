## System Operation #1:
`offerNewLesson(lessonType, mode);` 
#### Operation Contract:
`offerNewLesson`
#### Cross References:
Use case - Process Offerings
#### Preconditions:
- The various `lessonType` must be predefined
- `mode` should be one of the accepted lesson delivery modes
#### Postconditions:
- If `lessonType` is invalid, then an `InvalidLessonType` message is returned
- If `lessonType` is valid, then it will proceed to specify the location

## System Operation #2:
`SpecifyLocation(location);`
#### Operation Contract:
`SpecifyLocation`
#### Cross References:
Use case - Process  Offerings
#### Preconditions:
- The `location` provided exists and is located in the system
#### Postconditions:
- If the location is fully booked, then a `LocationFullyBooked` message is returned
- If the location is available, then timeslot selection process begins

## System Operation #3:
`SpecifyTimeSlots(schedule)`
#### Operation Contract:
`SpecifyTimeSlots`
#### Cross References:
Use Case - Process Offerings
#### Preconditions:
- `schedule` is valid and does not overlap with existing schedules
#### Postconditions:
- If the timeslots are valid, then proceed to search for available lessons
- A confirmation for time slots is provided
