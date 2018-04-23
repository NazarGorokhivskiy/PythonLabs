from Toy import *


class Car(Toy):
    toy_type = ToyType.car

    def __init__(self, size, age, is_cargo):
        self.size = size
        self.age = age
        self.is_cargo = is_cargo
