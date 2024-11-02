### Operation:
`searchAvailableOffer();`

### Cross References:
Use case - Process Bookings

### Preconditions:
- The `Client` is logged in
- The `Client` initiates a search request to view the available offerings
### Postconditions:
- System checks for available offers:
  - The system calls the `getAll()` operation on `Offering` to retrieve a list of offerings
- If the available offers are found:
  - `Offering` returns a list of available offers
  - The system displays the retrieved offers to the `Client`
  - The `Client` has the option to initiate a booking through `book(Offer, Client)` 
 - If no offers are found:
   - `Offering` will return message mentioning that no offers were available
   - The system then displays the no offers available message


