from SportToy import *
from Toy import *


class Ball(SportToy):
    toy_type = ToyType.ball

    def __init__(self, size, age, is_for_football):
        self.size = size
        self.age = age
        self.sport_type = SportType.ball_game
        self.is_for_football = is_for_football

