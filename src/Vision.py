# from Objet import Objet
from Static import Static

class Vision:

    def __init__(self, larg, long):
        self.grille = Static.createGrille(larg, long)
        self.larg = larg
        self.long = long