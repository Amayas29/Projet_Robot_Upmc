from Utils.tools import Point, Vecteur

class Robot:

    def __init__(self, center, longeur, largeur, vitesse):

        self.center = center
        self.longeur = longeur
        self.largeur = largeur

        self.chg = Point(center.x - longeur//2, center.y + largeur//2)
        self.cbg = Point(center.x - longeur//2, center.y - largeur//2)

        self.chd = Point(center.x + longeur//2, center.y + largeur//2)
        self.cbd = Point(center.x + longeur//2, center.y - largeur//2)

        self.angle = 0
        self.lspeed = 0
        self.rspeed = 0
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2
    

    def set_motor_dps(self, port, dps):

        if (port == self.MOTOR_LEFT):
            self.lspeed = dps

        elif(port == self.MOTOR_RIGHT):
            self.rspeed = dps

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.lspeed = dps
            self.rspeed = dps

        else:
            pass