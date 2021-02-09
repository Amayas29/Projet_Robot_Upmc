from tool import is_occupe, create_grille, normalise_angle
from robotsimu import RobotSimu
from math import sqrt

#représente la vision du robot, ce qu'il voit devant lui
class Vision:

    #Constructeur
    def __init__(self, larg, long):
        #crée une mini grille,copiant sur celle de simulation
        self.grille = create_grille(larg, long)
        self.larg = larg
        self.long = long


    #Determine si sur une distance donnee, il y a des obstacles ou non
    def libre_sur(self, x, taille_robot, angle):
        
        #verifie si le parametre est cohérent
        if(x > self.larg):
            print("Vision impossible !")
            return
        
        angle = normalise_angle(angle)
        if not (angle == 0 or angle == 90 or angle == 180 or angle == 270):
            taille_robot = round(sqrt(2) * taille_robot)

        pair = taille_robot % 2
        milieu = self.long // 2 - 1
        demi_taille = taille_robot // 2 
        debut = milieu - demi_taille
        fin = milieu + demi_taille + pair

        if angle >= 90 and angle <= 180:       
            debut += 1
            fin += 1

        for i in range(debut, fin):
            for j in range(x):
                if (is_occupe(self.grille,i,j)): #Regarde les cases remontant a partir du coin inférieur gauche grace a self.long - i
                        print("impossible il y a un objet ! sa position dans la vision est ",i,j)
                        return False
        print("On peut avancer !")
        return True
    
    def distance_max_obstacle(self):
        #return la distance max avant le premier obstacle rencontrer (en prenant en compte la largeur du robot)
        return 1
