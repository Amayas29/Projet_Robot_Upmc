from utils.tools import Segment
from utils.tools import Point
import random


class Obstacle:

    def __init__(self, src, dest):
        self.segment = Segment(src, dest)


class Gemme:

    def __init__(self):
        x = random.randint(100, 900)
        y = random.randint(50, 850)
        self.pos = Point(x, y)
        self.duree_vie = random.randint(10, 15)
