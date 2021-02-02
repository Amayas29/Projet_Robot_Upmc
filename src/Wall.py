from Objet import Objet

class Wall(Objet):

    def __init__(self):
        self.isFix = True

    def __str__(self):
        return "W"