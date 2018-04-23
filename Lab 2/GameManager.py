from Toy import *
from Car import *
from Doll import *
from SportToy import *
from Ball import *
from Hoop import *


class GameManager:
    toys = []

    def __init__(self):
        pass

    def sort_by_age(self):
        self.toys.sort()

    def find_by_group(self, age, size, toy_type):
        founded_toys = []

        for toy in self.toys:
            if toy.age == age or toy.size == size or toy.toy_type == toy_type:
                founded_toys.append(toy)

        return founded_toys

    def add_toy(self, toy):
        self.toys += toy


if __name__ == '__main__':
    manager = GameManager()

    car = Car(Age.preschooler, Size.small, True)
    doll = Doll(Age.preschooler, Size.medium, Sex.female)
    ball = Ball(Age.preschooler, Size.small, False)
    hoop = Hoop(Age.baby, Size.big, 228)

    manager.toys = [car, doll, ball, hoop]

    print(manager.find_by_group(Size.small, None, None))
    pass
