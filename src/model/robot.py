
from utils.tools import Point, Vecteur
from .vision import Vision
import math


class Robot:

    WHEEL_BASE_WIDTH = 60
    WHEEL_DIAMETER = 30
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi

    def __init__(self, center, arene):

        self.center = center

        self.vec_deplacement = Vecteur.get_vect_from_angle(0)
        self.refresh()

        self.lspeed = 0
        self.rspeed = 0
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2
        self.vec_servo = Vecteur.get_vect_from_angle(0)
        self.vision = Vision(arene)
        self.posr = 0
        self.posl = 0
        self.trait = False

    def offset_motor_encoder(self, port, offset):

        if (port == self.MOTOR_LEFT):
            self.posl += offset

        elif(port == self.MOTOR_RIGHT):
            self.posr += offset

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.posl += offset
            self.posr += offset

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
        return (self.posl, self.posr)

    def set_led(self, led, red=0, green=0, blue=0):
        print("Changement de la led {} à ({},{},{})".format(led, red, green, blue))

    def get_voltage(self):
        return 100

    def get_distance(self):
        self.vision.sync_vision(self)
        return self.vision.get_distance(self)

    def servo_rotate(self, position):
        position = -position
        vec_robot = Vecteur(self.chd, self.cbd)
        angle = Vecteur.get_vect_from_angle(0).angle_sign(vec_robot)
        self.vec_servo = Vecteur.get_vect_from_angle(position + angle)

    def stop(self):
        self.set_motor_dps(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)

    def get_image(self):
        return "Mon image est : 🤖"

    def __str__(self):
        return " ".join([str(self.chg), str(self.chd), str(self.cbd), str(self.cbg)])

    def refresh(self):
        center = self.center
        vec_norm = Vecteur(
            Point(0, 0), Point(- self.vec_deplacement.vect[1], self.vec_deplacement.vect[0]))

        self.chg = Point(center.x - (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[0] - (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[0],
                         center.y - (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[1] - (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[1])

        self.cbg = Point(center.x - (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[0] + (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[0],
                         center.y - (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[1] + (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[1])

        self.chd = Point(center.x + (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[0] - (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[0],
                         center.y + (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[1] - (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[1])

        self.cbd = Point(center.x + (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[0] + (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[0],
                         center.y + (self.WHEEL_BASE_WIDTH//2) * self.vec_deplacement.vect[1] + (self.WHEEL_BASE_WIDTH//2) * vec_norm.vect[1])

def dessin(self, boole):
  self.trait=boole
