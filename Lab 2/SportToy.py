from Toy import *


class SportType(Enum):
    ball_game = 1
    gymnastics = 2


class SportToy(Toy):
    sport_type = None
