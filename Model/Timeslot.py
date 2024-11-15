class Timeslot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def __eq__(self, other):
        if isinstance(other, Timeslot):
            return self.start_time == other.start_time and self.end_time == other.end_time
        return False
