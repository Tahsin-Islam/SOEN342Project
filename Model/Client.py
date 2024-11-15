from dataclasses import dataclass

@dataclass
class Client:
    name: str
    age: int
    phone_number: str

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (self.name == other.name and
                self.age == other.age and
                self.phone_number == other.phone_number)
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
