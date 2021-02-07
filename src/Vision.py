from Tool import *
from RobotSimu import RobotSimu

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
        
        if(x > self.larg):
            print("Vision impossible !")
            return
        
        for i in range(self.long//2 - self.tailleRob//2,self.long//2 + self.tailleRob//2):
            for j in range(x):
                if (is_Occupe(self.grille,i,j)): #Regarde les cases remontant a partir du coin inférieur gauche grace a self.long - i
                        print("impossible il y a un objet !")
                        # self.grille[i][j] = "K"
                        affiche(self.grille)
                        return False
        print("On peut avancer !")
        return True
    
    def distanceMaxObstacle(self):
        #return la distance max avant le premier obstacle rencontrer (en prenant en compte la largeur du robot)
        return 1
