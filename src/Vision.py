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
        # if(x <= len(self.grille[0])):
        #     for i in range(0,x): #Boucle parcourant la distance de 0 jusqu'à x 
        #         for j in range(0,self.tailleRob): #Boucle parcourant la taille du robot
        #             if (is_Occupe(self.grille,j,self.long-i)): #Regarde les cases remontant a partir du coin inférieur gauche grace a self.long - i
        #                 print("impossible il y a un objet !")
        #                 return False
        #     print("On peut avancer !")
        #     return True
        # else:
        #     print("Vision impossible !")
        if(x > self.larg):
            print("Vision impossible !")
            return
        
        for i in range(self.long//2 - self.tailleRob//2,self.long//2 + self.tailleRob//2):
            for j in range(x):
                if (is_Occupe(self.grille,j,i)): #Regarde les cases remontant a partir du coin inférieur gauche grace a self.long - i
                        print("impossible il y a un objet !")
                        return False
        print("On peut avancer !")
        return True
    
    def distanceMaxObstacle(self):
        #return la distance max avant le premier obstacle rencontrer (en prenant en compte la largeur du robot)
        return 1
