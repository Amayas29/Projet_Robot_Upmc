from Utils.tools import Segment

class Obstacle:

    def __init__(self, src, dest):

        self.segment = Segment(src, dest)