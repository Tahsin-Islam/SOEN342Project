from enum import Enum


class LessonType(Enum):
    YOGA = 1
    KARATE = 2
    DANCE = 3
    SWIMMING = 4

class Lesson:
    def __init__(self, lesson_type: LessonType, mode: bool):
        self._lesson_type = lesson_type
        self._mode = mode

    @property
    def lesson_type(self):
        return self._lesson_type

    @lesson_type.setter
    def lesson_type(self, lesson_type: LessonType):
        self._lesson_type = lesson_type

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: bool):
        self._mode = mode

    def __eq__(self, other):
        if isinstance(other, Lesson):
            return self._lesson_type == other._lesson_type and self._mode == other._mode
        return False
