# from Objet import Objet
from Static import Static
class Vision:
    def __init__(self, larg, long):
        self.grille = Static.createGrille(larg, long)
        self.larg = larg
        self.long = long

    def add_Objet(self, objet, x, y):
        """Assuming objet is type Objet"""
        if ( 0 <= x < self.larg ) and ( 0 <= y < self.long ) and ( self.is_Occupe(x,y) == False ) :
            self.grille[x][y] = objet
            return self.is_Occupe( x, y)
        return False

    def is_Occupe(self, x, y):
        return self.grille[x][y]!=None
