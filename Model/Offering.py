class Offering:
    def __init__(self, is_full: bool, is_group_offering: bool, lesson_type):
        self.is_full = is_full
        self.is_group_offering = is_group_offering
        self.lesson_type = lesson_type

    def is_full(self):
        return self.is_full

    def is_group_offering(self):
        return self.is_group_offering

    def get_lesson_type(self):
        return self.lesson_type

    def set_full(self, full: bool):
        self.is_full = full

    def set_group_offering(self, group_offering: bool):
        self.is_group_offering = group_offering

    def set_lesson_type(self, lesson_type):
        self.lesson_type = lesson_type

    def equals(self, another_offering) -> bool:
        return (
            self.is_full == another_offering.is_full and
            self.is_group_offering == another_offering.is_group_offering and
            self.lesson_type == another_offering.lesson_type
        )
