from utils.tools import Point, Vecteur
from .vision import Vision
import math


class Robot:

    WHEEL_BASE_WIDTH = 117
    WHEEL_DIAMETER = 66.5
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi

    def __init__(self, center, longeur, largeur):

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
        self.vision = Vision(10)
        self.posr = 0
        self.posl = 0

    def offset_motor_encoder(self, port, offset):

        if (port == self.MOTOR_LEFT):
            self.posl = offset

        elif(port == self.MOTOR_RIGHT):
            self.posr = offset

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.posl = offset
            self.posr = offset

    def set_motor_dps(self, port, dps):

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

    def set_led(self, led, red=0, green=0, blue=0):
        print(f"Changement de la led {led} à ({red},{green},{blue})")

    def get_voltage(self):
        return 100

    def get_distance(self):
        return self.vision.get_distance()

    def servo_rotate(self, position):
        # Pour tourner le servo !
        pass

    def stop(self):
        self.set_motor_dps(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)

    def get_image(self):
        return "Mon image est : 🤖"
