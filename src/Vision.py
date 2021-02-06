from Tool import *

#représente la vision du robot, ce qu'il voit devant lui
class Vision:

    #Constructeur
    def __init__(self, larg, long, tailleRob):
        #crée une mini grille,copiant sur celle de simulation
        self.grille = createGrille(larg, long)
        self.larg = larg
        self.long = long
        self.tailleRob = tailleRob


    #Determine si sur une distance donnee, il y a des obstacles ou non
    def libresur(self, x):
        return True

    
    def distanceMaxObstacle(self):
        #return la distance max avant le premier obstacle rencontrer (en prenant en compte la largeur du robot)
        return 1
