from Objet import Objet

class RobotSimu(Objet):

    def __init__(self):
        self.isFix = False
        #angle en degres
        self.dirrection = 0
        self.posx = None
        self.posy = None
    

    def setPos(self, x, y, dir):
        """assuming dir is between 0 and 360"""
        if x >= 0 and y >= 0 and 0 <= dir <= 360:
            self.dirrection = dir
            self.posx = x
            self.posy = y
        else:
            print("ERREUR x ou y < 0")


    def __str__(self):
        return "R"
