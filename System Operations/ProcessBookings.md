## System Operation #1:
`searchAvailableOffer();`
#### Operation Contract:
`searchAvailableOffer`
#### Cross References:
Use case - Process Bookings

#### Preconditions:
- The `Client` is logged in
- The `Client` initiates a search request to view the available offerings
#### Postconditions:
- If the available offers exist, the system retrieves and displays a list of offers
- If no offers are available, the system returns a `NoOffersAvailable` message

## System Operation #2:
`book(Offer, Client);`
#### Operation Contract:
`book`
#### Cross References:
Use case - Process Bookings
#### Preconditions:
- The `Offer` exists and is available
- The `Client` has selected an offer to book
- The `Client` is 18+ or has a guardian
#### Postconditions:
- A `Booking` object is created and linked to `Client` and `Offer`
- `Booking` is stored in the system
- Confirmation and booking details are returned to `Client`

## System Operation #3:
`getOwnBooking(Client);`
#### Operation Contract:
`getOwnBooking`
#### Cross References:
Use case - Process Bookings
#### Preconditions:
- `Client` is logged in
#### Postconditions:
- System retrieves all bookings associated with `Client`
- List of bookings displayed to `Client`

## System Operation #4:
`cancelBooking(Booking);`
#### Operation Contract:
`cancelBooking`
#### Cross References:
Use case: Process Bookings
#### Preconditions:
- The `Client` has existing `Booking`
#### Postconditions:
- Specified `Booking` labeled cancelled in the system
- System sends cancellation confirmation message to `Client`


