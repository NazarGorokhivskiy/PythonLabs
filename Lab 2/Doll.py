from enum import Enum
from Toy import *


class Sex(Enum):
    male = 1
    female = 2


class Doll(Toy):
    toy_type = ToyType.doll

    def __init__(self, size, age, sex):
        self.size = size
        self.age = age
        self.sex = sex
