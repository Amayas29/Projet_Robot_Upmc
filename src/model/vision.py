from math import e
from utils.tools import Point, Droite, Vecteur
from model.obstacles import Balise
from copy import deepcopy


class Vision:

    """
        La vision du robot en mode simulation

        Elle contient une liste des elements selectionne suivant le vecteur servo du robot

        Elle permet de calculer le get_distance et detecter la balise
    """

    GAUCHE = 1
    DROITE = 0

    DISTANCE = float("inf")

    def __init__(self, arene):
        self.elements = []
        self.arene = arene
        self.balise = None

    def sync_vision(self, robot):
        """
        robot -> None
        Elle permet d'actualiser les elements de la vision
        """

        self.elements = []
        self.balise = None

        largeur = robot.WHEEL_BASE_WIDTH

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)
        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        vec_norme = Vecteur(a, b)
        left_droite = Droite.get_droite(vec_norme, a)
        right_droite = Droite.get_droite(vec_norme, b)

        for elem in self.arene.elements:

            seg = elem.segment
            new_vec_src = Vecteur(new_milieu, seg.src)
            new_vec_dest = Vecteur(new_milieu, seg.dest)

            if vec_src.angle(new_vec_src) > 90 and vec_src.angle(new_vec_dest) > 90:
                continue

            if seg.intersection(a, vec_src) is not None or seg.intersection(b, vec_src) is not None:

                seg_droite = seg.to_droite()
                if min(a.distance_to_droite(seg_droite), b.distance_to_droite(seg_droite)) > self.DISTANCE:
                    continue

                if isinstance(elem, Balise):
                    self.balise = elem

                self.elements.append(elem)
                continue

            if max(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)) > largeur \
                    or max(seg.dest.distance_to_droite(left_droite), seg.dest.distance_to_droite(right_droite)) > largeur:
                continue

            if isinstance(elem, Balise):
                self.balise = elem

            self.elements.append(elem)

    def get_distance(self, robot):
        """
        robot -> None

        Permet de calculer la distance à l'obstacle le plus proche du robot
        """

        largeur = robot.WHEEL_BASE_WIDTH

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)
        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        mini = float("inf")
        for elem in self.elements:
            seg = elem.segment

            p1 = seg.intersection(new_milieu, vec_src)

            dist = float("inf")
            if p1 is not None:
                dist = p1 - new_milieu

            mini = min(mini, dist)

        return mini

    def __str__(self):
        """
        None -> str
        Affiche la liste des elements selectionnes
        """
        s = ""
        for elem in self.elements:
            s += str(elem) + ", "
        return s

    def get_angle_orientation_balise(self, robot):
        """
        robot -> float * float

        Calcule l'angle et l'orientation de la balise par apport au robot
        """

        if self.balise is None:
            return -1, -1

        largeur = robot.WHEEL_BASE_WIDTH

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)

        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        milieu_balise = Point.milieu(
            self.balise.segment.src, self.balise.segment.dest)

        vec_balise = Vecteur(new_milieu, milieu_balise)

        angle = vec_src.angle_sign(vec_balise)

        if angle >= 0:
            return angle, self.DROITE

        return -angle, self.GAUCHE
