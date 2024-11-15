class Booking:
    def __init__(self, booking_number):
        self.booking_number = booking_number

    def get_booking_number(self):
        return self.booking_number

    def set_booking_number(self, booking_number):
        self.booking_number = booking_number

    def __eq__(self, other):
        if isinstance(other, Booking):
            return self.booking_number == other.booking_number
        return False

