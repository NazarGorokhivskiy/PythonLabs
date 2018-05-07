from enum import Enum, IntEnum


class Size(Enum):
    small = 1
    medium = 2
    big = 3


class Age(IntEnum):
    baby = 1
    preschooler = 2
    schooler = 3


class ToyType(Enum):
    doll = 1
    car = 2
    hoop = 3
    ball = 4


class Toy:
    price = 0.0
    age = None
    size = None
    toy_type = None

    def __str__(self):
        return self.__class__.__name__ + ": " + "Size: " + self.size.name + ", Age: " + self.age.name
