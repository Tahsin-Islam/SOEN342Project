from typing import List

class Instructor:
    def __init__(self, name: str, phone_number: str, specialization: List[str], start_date: str, end_date: str):
        self.name = name
        self.phone_number = phone_number
        self.specialization = specialization
        self.start_date = start_date
        self.end_date = end_date

    def get_name(self) -> str:
        return self.name

    def get_phone_number(self) -> str:
        return self.phone_number

    def get_specialization(self) -> List[str]:
        return self.specialization

    def get_start_date(self) -> str:
        return self.start_date

    def get_end_date(self) -> str:
        return self.end_date

    def set_name(self, name: str):
        self.name = name

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number

    def set_specialization(self, specialization: List[str]):
        self.specialization = specialization

    def set_start_date(self, start_date: str):
        self.start_date = start_date

    def set_end_date(self, end_date: str):
        self.end_date = end_date

    def __eq__(self, other) -> bool:
        if not isinstance(other, Instructor):
            return False
        return (self.name == other.name and
                self.phone_number == other.phone_number and
                self.specialization == other.specialization and
                self.start_date == other.start_date and
                self.end_date == other.end_date)
