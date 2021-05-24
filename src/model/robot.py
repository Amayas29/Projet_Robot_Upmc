
from utils.tools import Point, Vecteur
from .vision import Vision
import math


class Robot:

    # Les meta donnes du robot
    WHEEL_BASE_WIDTH = 60
    WHEEL_DIAMETER = 30
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi

    def __init__(self, center, arene):

        # Le center du robot
        self.center = center

        # On calcule le vecteur deplacement du robot ainsi que les coordonnees de tous les coté
        self.vec_deplacement = Vecteur.get_vect_from_angle(0)
        self.refresh()

        # On initialise les differents champs
        self.lspeed = 0
        self.rspeed = 0
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2

        self.LED_LEFT_EYE = 1
        self.LED_RIGHT_EYE = 2

        self.vec_servo = Vecteur.get_vect_from_angle(0)
        self.vision = Vision(arene)
        self.posr = 0
        self.posl = 0
        self.crayon = False
        self.image = None

        self.led_color = (0, 0, 0, 255)

    def offset_motor_encoder(self, port, offset):
        """
            int * float -> None

            Permet de mettre à jour les position des roues
        """

        if (port == self.MOTOR_LEFT):
            self.posl += offset

        elif(port == self.MOTOR_RIGHT):
            self.posr += offset

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.posl += offset
            self.posr += offset

    def set_motor_dps(self, port, dps):
        """
        int * float -> None

        Permet de changer la vitesse des roues du robot
        """

        if (port == self.MOTOR_LEFT):
            self.lspeed = dps

        elif(port == self.MOTOR_RIGHT):
            self.rspeed = dps

        elif (port == self.MOTOR_LEFT + self.MOTOR_RIGHT):
            self.lspeed = dps
            self.rspeed = dps

    def get_motor_position(self):
        """
        None -> float * float
        Permet de reccuperer les positions des roues
        """
        return (self.posl, self.posr)

    def set_led(self, led, red=0, green=0, blue=0):
        """
            int * float * float * float -> None

            Affiche un message de changement de couleur pour la led
        """
        self.led_color = (red, green, blue)

    def get_distance(self):
        """
        None -> float
        Reccupere la distance à l'obstacle le plus proche du robot
        """
        self.vision.sync_vision(self)
        return self.vision.get_distance(self)

    def servo_rotate(self, position):
        """
        float -> None
        Permet de tourner le servo du robot, donc mettre à jour le vecteur servo du robot
        """

        position = -position
        vec_robot = Vecteur(self.chd, self.cbd)
        angle = Vecteur.get_vect_from_angle(0).angle_sign(vec_robot)
        self.vec_servo = Vecteur.get_vect_from_angle(position + angle)
        self.vision.sync_vision(self)

    def stop(self):
        """
        None -> None
        Arrete le robot
        """
        self.set_motor_dps(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)

    def get_angle_orientation_balise(self):
        """
        None -> float * float
        Retourne l'angle et l'orientation de la balise par apport au robot
        """
        return self.vision.get_angle_orientation_balise(self)

    def __str__(self):
        """
        None -> str
        Representation textuelle du robot
        """
        return " ".join([str(self.chg), str(self.chd), str(self.cbd), str(self.cbg)])

    def refresh(self):
        """
        None -> None

        Mets à jour les coordonnees des differents coté du robot
        """
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

    def up(self):
        """
        None -> None
        Leve le crayon de dessin
        """
        self.crayon = False

    def down(self):
        """
        None -> None
        Baisse le crayon de dessin
        """
        self.crayon = True

    def set_image(self, frame):
        self.image = frame

    def get_image(self):
        return self.image
