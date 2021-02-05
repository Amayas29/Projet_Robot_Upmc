# from Objet import Objet
from Static import Static

#représente la vision du robot, ce qu'il voit devant lui
class Vision:

    #Constructeur
    def __init__(self, larg, long, tailleRob):
        #crée une mini grille,copiant sur celle de simulation
        self.grille = Static.createGrille(larg, long)
        self.larg = larg
        self.long = long
        self.tailleRob = tailleRob

    #Determine si sur une distance donnee, il y a des obstacles ou non
    def libresur(self, x):
        return True
