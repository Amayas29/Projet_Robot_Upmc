from objet import Objet

#crée un mur
class Wall(Objet):

    def __init__(self):
        super().__init__()
        self.is_fix = True # c'est un objet fixe


    def __str__(self):
        return "W" #permet de le visualiser sur la simulation
