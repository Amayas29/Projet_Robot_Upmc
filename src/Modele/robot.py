from Utils.tools import Point, Vecteur
from vision import Vision
from datetime import datetime

class Robot:

    def __init__(self, center, longeur, largeur, vitesse):

        self.center = center
        self.longeur = longeur
        self.largeur = largeur

        self.chg = Point(center.x - longeur//2, center.y + largeur//2)
        self.cbg = Point(center.x - longeur//2, center.y - largeur//2)

        self.chd = Point(center.x + longeur//2, center.y + largeur//2)
        self.cbd = Point(center.x + longeur//2, center.y - largeur//2)

        self.lspeed = 0
        self.rspeed = 0
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2
        self.vec_servo = Vecteur.get_vect_from_angle(0)
        self.vec_deplacement = Vecteur.get_vect_from_angle(0)
        self.vision = Vision(5)
        self.initial_time = None
        self.posr = 0
        self.posl = 0
    
    def offset_motor_encoder(self, port, offset):

        self.initial_time = datetime.now()
        
        if (port == self.MOTOR_LEFT):
            self.posl = offset

        elif(port == self.MOTOR_RIGHT):
            self.posr = offset

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.posl = offset
            self.posr = offset 
        
    def set_motor_dps(self, port, dps):

        if self.initial_time is None:
            self.initial_time = datetime.now()

        if (port == self.MOTOR_LEFT):
            self.lspeed = dps

        elif(port == self.MOTOR_RIGHT):
            self.rspeed = dps

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.lspeed = dps
            self.rspeed = dps

    def get_motor_position(self):
        # Voir l'ordre
        return (self.posr, self.posl)        