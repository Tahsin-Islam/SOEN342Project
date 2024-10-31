package Model;

public class Booking {
    private int bookingNumber;

    public Booking(int bookingNumber){
        this.bookingNumber = bookingNumber;
    }

    public int getBookingNumber() {
        return bookingNumber;
    }

    public void setBookingNumber(int bookingNumber) {
        this.bookingNumber = bookingNumber;
    }


    public boolean equals(Booking anotherBooking) {
        return this.bookingNumber == anotherBooking.bookingNumber;
    }
}
