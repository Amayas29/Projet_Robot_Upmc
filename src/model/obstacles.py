from utils.tools import Segment


class Obstacle:

    def __init__(self, src, dest):
        self.segment = Segment(src, dest)


class Balise(Obstacle):

    def __init__(self, src, dest):
        super().__init__(src, dest)
