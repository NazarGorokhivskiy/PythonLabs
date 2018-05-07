from Ball import *
from Car import*
from Doll import *
from GameManager import *
from Hoop import *

manager = GameManager()

car = Car(Size.small, Age.schooler, True)
doll = Doll(Size.medium, Age.preschooler, Sex.female)
ball = Ball(Size.small, Age.preschooler, False)
hoop = Hoop(Size.big, Age.baby, 228)
manager.toys = [car, doll, ball, hoop]

manager.sort_by_age()
manager.print_list()

manager.toys = manager.find_by_group(Size.small, None, None)
manager.print_list()
