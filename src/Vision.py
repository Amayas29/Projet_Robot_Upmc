# from Objet import Objet
from Static import Static

class Vision:

    def __init__(self, larg, long, tailleRob):
        self.grille = Static.createGrille(larg, long)
        self.larg = larg
        self.long = long
        self.tailleRob = tailleRob

    
    def libresur(self, x):
        return True