from time import sleep
from datetime import datetime
from utils.tools import Vecteur, Point
from math import pi
from .obstacles import Balise


class Arene:

    """ 
        L'arene represente le modele de notre code, elle permet de faire deplacer le robot sur l'arene et stocker les obstacles et la balise
    """

    def __init__(self):
        # La liste des obstacles
        self.elements = []

        self.robot = None

        # Le dernier instant lors de l'appel asynchrone
        self.temps_precedent = None
        self.angle_parcouru = 0
        self.balise = None
        self.run = True

    def boucle(self, fps):
        """
        float -> None
        La boucle de mise à jour de l'arene dans un thread
        """
        if self.robot is None:
            return

        while self.run:
            self.update()
            sleep(1./fps)

    def update(self):
        """
        None -> None
        Permet de mettre à jour l'arene
        """

        # Si c'est le premier appel on initialise le temps_precedent
        if self.temps_precedent is None:
            self.temps_precedent = datetime.now()

        # On calcule le temps passé du dernier appel à l'appel courrant
        now = datetime.now()
        diff_temps = (now - self.temps_precedent).total_seconds()
        self.temps_precedent = now

        if self.robot.lspeed == 0 and self.robot.rspeed == 0:
            return

        # Si on a les memes vitesse : donc avancer tout droite
        if self.robot.lspeed == self.robot.rspeed:

            # On calcule l'angle avec lequel les roue vont tournes
            angle_roue = diff_temps * self.robot.lspeed

            # On calcule la distance parcourue
            k = angle_roue // 360
            r = angle_roue % 360

            distance = k * self.robot.WHEEL_CIRCUMFERENCE + \
                (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

            # On mets à jour les positions des roues pour le robot
            self.robot.posr += angle_roue
            self.robot.posl += angle_roue

            # On calcule le point de translation du mouvement
            x = self.robot.vec_deplacement.vect[0] * distance
            y = self.robot.vec_deplacement.vect[1] * distance

            point_tmp = Point(x, y)

            # On deplace le robot et on re-calcule toutes ses coordonnees
            self.robot.center + point_tmp
            self.robot.refresh()
            return

        # Sinon le robot tourne dans une direction
        if self.robot.lspeed == 0 and self.robot.rspeed != 0:

            # On calcule le point de rotation
            roue = Point.milieu(self.robot.chg, self.robot.chd)

            # Ainsi que l'angle avec lequel les roues vont tourner
            angle_roue = diff_temps * self.robot.rspeed

            # On actualise la position de la roue
            self.robot.posr += angle_roue

        # De maniere symetrique
        elif self.robot.rspeed == 0 and self.robot.lspeed != 0:
            roue = Point.milieu(self.robot.cbg, self.robot.cbd)
            angle_roue = diff_temps * self.robot.lspeed
            self.robot.posl += angle_roue

        # On calcule la distance à parcourir
        k = angle_roue // 360
        r = angle_roue % 360

        distance = k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

        # On calcule l'angle de rotation du robot
        angle = distance * 180 / (pi * self.robot.WHEEL_BASE_WIDTH)

        if self.robot.lspeed == 0 and self.robot.rspeed != 0:
            angle = -angle

        # On actualise l'angle parcouru du robot
        self.angle_parcouru += angle

        # On mets à jour le vecteur deplacement du robot
        self.robot.vec_deplacement = Vecteur.get_vect_from_angle(
            self.angle_parcouru)

        # On fait une rotation du robot par apport au point calculer ainsi que l'angle, ensuite on re-calcule toutes ses coordonnees
        self.robot.center.rotate(roue, angle)
        self.robot.refresh()

    def set_robot(self, robot):
        """
        Robot -> None

        Permet de setter un robot à l'arene
        """
        if robot != None:
            self.robot = robot

    def add_obstacle(self, obstacle):
        """
        Obstacle -> None
        Permet d'ajouter un obstacle dans l'arene
        """
        if obstacle != None:
            self.elements.append(obstacle)

    def set_balise(self, balise):
        """
        Balise -> None

        Permet de setter la balise à l'arene
        """

        if balise != None and isinstance(balise, Balise):
            self.elements.append(balise)
            self.balise = balise

    def stop(self):
        """
        None -> None
        Permet d'arrete la boucle de l'arene (la boucle du thread)
        """
        self.run = False
