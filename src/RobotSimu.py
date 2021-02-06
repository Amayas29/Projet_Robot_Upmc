from Objet import Objet

#Classe robot simuulation qui hérite de objet
class RobotSimu(Objet):

    #Constructeur
    def __init__(self):
        self.isFix = False
        #angle en degres
        self.direction = 0
        self.posx = None
        self.posy = None
    

    def setPos(self, x, y, dir):
        #pose le robot sur les positions x et y de la grille de la simulation 
        """assuming dir is between 0 and 360"""
        if x >= 0 and y >= 0 and 0 <= dir <= 360:
            self.direction = dir
            self.posx = x
            self.posy = y
        else:
            print("ERREUR x ou y < 0")


    def __str__(self):
        #permet d'afficher le robot sur la simulation avec la lettre R
        return "R"
