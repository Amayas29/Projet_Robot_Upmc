import cv2
from math import atan2, degrees
from model.robot import Robot


def color_profiles(n):
    """
    Fonction qui retourne les condition des couleurs
    """
    if n == 0:
        name = "Bleu"
        hsv_lower = (95, 100, 20)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 1:
        name = "Rouge"
        hsv_lower = (0, 100, 50)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 2:
        name = "Vert"
        hsv_lower = (50, 50, 20)
        hsv_upper = (100, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 3:
        name = "Jaune"
        hsv_lower = (10, 100, 50)
        hsv_upper = (50, 255, 255)
        return (name, hsv_lower, hsv_upper)


def get_masks_color(frame):
    """
    Image -> List * int
    Permet de reccuperer les masks de l'image apres applications de la selection des couleurs ainsi que le nombre de masks non vides
    """
    masks = []

    # On transforme l'image en hvs
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Le nombre de masks non vides
    number = 0

    # On boucle sur les quatre couleurs
    for i in range(4):

        # On reccuper les conditions de la couleur i
        _, hsv_lower, hsv_upper = color_profiles(i)

        # On selectionne les pixels qui verifie les conditions
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

        # On netoie un peu le mask
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)

        # On chercher toutes les formes detecter
        elements, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Si on a trouver au moins element, donc le mask n'est pas vide on increment le nombre
        if len(elements) > 0:
            number += 1

        # On ajoute le mask obtenu
        masks.append(mask)

    return masks, number


def get_position_balise(frame):
    """
    Image -> float * float

    Permet de reccuperer la position de la balise dans l'image
    """

    # On reccuperer les masks
    masks, number = get_masks_color(frame)

    # Si on a moins de 3 masks non vide donc la balise n'existe pas dans l'image
    if number < 3:
        return -1, -1

    # On join tout les masks
    mask = (masks[0] | masks[1]) | (masks[2] | masks[3])

    # On netoie le mask final
    mask = cv2.erode(mask, None, iterations=4)
    mask = cv2.dilate(mask, None, iterations=4)

    # On reccupere les formes detecter
    elements, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # On extrait le max de ces elements (c'est la balise)
    c = max(elements, key=cv2.contourArea)

    # On approche la forme par un cercle et on reccupere son centre et rayon
    ((x, y), _) = cv2.minEnclosingCircle(c)

    # On rectourne le centre
    return x, y


class Wrapper(object):
    """
        Un proxy pour mettre en commun les fonctions de la simulation et de l'irl
    """

    GAUCHE = 1
    DROITE = 0

    def __init__(self, robot):
        self.robot = robot

        # Un dictionnaire pour garder les donnés initiale pour chaque startegie
        self.liste_ref = {}
        self.WHEEL_BASE_CIRCUMFERENCE = robot.WHEEL_BASE_CIRCUMFERENCE

    def begin(self, ref, port):
        """
        hash * int -> None
        Permet de sauvegarder ls données initiale du robot pour la strategie donnée par sa reference
        """
        self.liste_ref[ref] = self.robot.get_motor_position()[port]

    def get_distance_parcouru(self, ref, port):
        """
        hash * int -> float
        Permet de reccuperer la distance parcourue pour la strategie donnée par sa reference
        """

        # On calculer la difference entre les donnée actual et les derniers données sauvegarder
        diff = self.robot.get_motor_position()[port] - self.liste_ref[ref]

        # On actualise les donnes sauvegardee
        self.liste_ref[ref] = self.robot.get_motor_position()[port]

        # On calcule la distance parcoure
        k = diff // 360
        r = diff % 360

        return k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

    def avancer(self, vitesse):
        """
        float -> None
        Permet au robot d'avancer d'une vitesse
        """
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, vitesse)

    def stop(self):
        """
        None -> None
        Arrete le robot
        """
        self.robot.stop()

    def tourner_servo(self, angle):
        """
        float -> None
        Tourne le servo du robot avec un angle
        """
        self.robot.servo_rotate(angle)

    def get_distance(self):
        """
        None -> float
        Retourne la distance à l'obstacle le plus proche
        """
        return self.robot.get_distance()

    def tourner(self, cote, vitesse):
        """
        int * float -> None

        Permet de tourner le robot vers un vote avec une vitesse
        """
        if cote == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, vitesse)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, vitesse)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)

    def get_angle_orientation_balise(self, image_loader=None):
        """
            [ImageLoader] -> float * int

            Retourne l'angle et l'orientation de la balise par apport au robot
        """

        # Si c'est le mode simulation
        if isinstance(self.robot, Robot):
            return self.robot.get_angle_orientation_balise()

        # Sinon on reccupere l'image d" l'image_loader si il existe sinon directement du robot
        if image_loader is None:
            frame = self.robot.get_image()
        else:
            frame = image_loader.get_image()

        # Si on a rien reccuperer alors la balise n'existe pas
        if frame is None:
            return -1, -1

        # On reccupere la position de la balise dans l'image
        (x, y) = get_position_balise(frame)

        # Si x = -1 alors la balise n'existe pas
        if x == -1:
            return -1, -1

        # On calcule l'angle et l'orientation de la balise
        y = frame.shape[1] - y

        sign = x - (frame.shape[0] / 2)
        orientation = self.GAUCHE if sign < 0 else self.DROITE

        if y == 0:
            return 90, orientation

        angle = atan2(abs(sign), y)

        return degrees(angle), orientation
