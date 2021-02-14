from objet import Objet
from tool import normalise_angle

#Classe robot simuulation qui hérite de objet
class RobotSimu(Objet):

    #Constructeur
    def __init__(self):
        super().__init__()
        #angle en degres
        self.direction = 0

    def set_pos(self, x, y, dir):
        #pose le robot sur les positions x et y de la grille de la simulation 
        """assuming dir is between 0 and 360"""
        dir = normalise_angle(dir)
        if x >= 0 and y >= 0:
            self.direction = dir
            self.posx = x
            self.posy = y
        else:
            print("ERREUR x ou y < 0")


    def __str__(self):
        #permet d'afficher le robot sur la simulation avec la lettre RR
        return "RR"
