from Objet import Objet

#crée un mur
class Wall(Objet):

    def __init__(self):
        self.isFix = True #c'est un objet fixe

    def __str__(self):
        return "W" #permet de le visualiser sur la simulation
