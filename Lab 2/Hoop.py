from SportToy import *
from Toy import *


class Hoop(SportToy):
    toy_type = ToyType.hoop

    def __init__(self, size, age, radius):
        self.size = size
        self.age = age
        self.sport_type = SportType.gymnastics
        self.radius = radius
