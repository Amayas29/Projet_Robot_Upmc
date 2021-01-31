from Objet import Objet

class RobotSimu(Objet):

    def __init__(self):
        self.isFix = False
        #North N Sud S Est E West W
        self.dirrection = "N"
        self.posx = None
        self.posy = None
    

    def setPos(self, x, y, dir):
        """assuming dir is N or S or E or W"""
        if x >= 0 and y >= 0:
            self.dirrection = dir
            self.posx = x
            self.posy = y
        else:
            print("ERREUR x ou y < 0")


    def __str__(self):
        return "R"