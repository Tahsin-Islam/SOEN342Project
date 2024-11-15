from enum import Enum

class SpaceType(Enum):
    POOL = "POOL"
    GYM = "GYM"
    STUDIO = "STUDIO"

class Location:
    def __init__(self, name, address, city, space_type, capacity):
        self._name = name
        self._address = address
        self._city = city
        self._space_type = space_type
        self._capacity = capacity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def space_type(self):
        return self._space_type

    @space_type.setter
    def space_type(self, value):
        self._space_type = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    def __eq__(self, other):
        if isinstance(other, Location):
            return (self._name == other._name and
                    self._address == other._address and
                    self._city == other._city and
                    self._space_type == other._space_type and
                    self._capacity == other._capacity)
        return False
