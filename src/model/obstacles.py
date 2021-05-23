from utils.tools import Segment


class Obstacle:
    """
        Les obstacles de la simulation

        Un obstacle est un segment de droite
    """

    def __init__(self, src, dest):
        self.segment = Segment(src, dest)


class Balise(Obstacle):
    """
        La balise de la simualtion est un type d'obstacle
    """

    def __init__(self, src, dest):
        super().__init__(src, dest)
