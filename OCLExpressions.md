Requirement 1
-------------
Offerings are unique. In other words, multiple offerings on the same day and time slot must be offered at a different location.
</br>
</br>
```context Offering:```</br>
&emsp;&emsp;```inv: Offering.allInstances() -> forAll(o1, o2 | o1 <> o2 and o1.date = o2.date and o1.startTime = o2.startTime and o1.endTime = o2.endTime implies o1.location <> o2.location ```

Requirement 2
-------------
Any client who is underage must necessarily be accompanied by an adult who acts as their guardian.
</br>
</br>
```context Client:```</br>
&emsp;&emsp;```inv: self.age < 18 implies self.guardian -> notEmpty()```

Requirement 3
-------------
The city associated with an offering must be one the city’s that the instructor has indicated in their availabilities.
</br>
</br>
```context Offering:```</br>
&emsp;&emsp;```inv: self.instructor.availableCities -> includes(self.city) ```

Requirement 4
-------------
A client does not have multiple bookings on the same day and time slot.
</br>
</br>
```context Client:```</br>
&emsp;&emsp;```inv:self.bookings -> forAll(b1, b2 | b1 <> b2 imples b1.date <> b2.date and b1.timeSlot <> b2.timeSlot ```
  
