class Schedule:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def __eq__(self, other):
        if isinstance(other, Schedule):
            return self.start_date == other.start_date and self.end_date == other.end_date
        return False
