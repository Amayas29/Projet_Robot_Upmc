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
        # On recupere le vecteur de la droite  faciale du robot
        vec_norme = Vecteur(robot.chd, robot.cbd)

        # On recupere le vecteur servo du robot
        vec_src = robot.vec_servo

        # On recupere le segment perpendiculaire a la droite du vecteur servo et qui passe par l'un des cotes du robot
        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        # On recupere le point d'intersection entre la droite du servo et le nouveau segment
        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)
        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        # On cree un vecteur du nouveau segment
        vec_norme = Vecteur(a, b)

        # On construit les extremites de la vision
        left_droite = Droite.get_droite(vec_norme, a)
        right_droite = Droite.get_droite(vec_norme, b)

        # On parcours tous les elements de l'arene
        for elem in self.arene.elements:

            # On recupere les vecteur de la nouvelle tete du robot vers les deux points points de l'obstacle
            seg = elem.segment
            new_vec_src = Vecteur(new_milieu, seg.src)
            new_vec_dest = Vecteur(new_milieu, seg.dest)

            # Si l'obstacle est derriere le robot on ne l'ajoute pas
            if vec_src.angle(new_vec_src) > 90 and vec_src.angle(new_vec_dest) > 90:
                continue

            # Si le on a une intersection entre l'obstacle et les droite des extremites de la vision
            if seg.intersection(a, vec_src) is not None or seg.intersection(b, vec_src) is not None:

                seg_droite = seg.to_droite()

                # Si l'obstacle est trop loin du robot on l'ajoute pas
                if min(a.distance_to_droite(seg_droite), b.distance_to_droite(seg_droite)) > self.DISTANCE:
                    continue

                # Si c'est la balise(objet a trouver) on la recupere
                if isinstance(elem, Balise):
                    self.balise = elem

                # On ajoute l'element dans la liste
                self.elements.append(elem)
                continue

            # Si l'objet n'intersecte pas les droite donc si l'obstacle est en dehors de la vision on l'ajoute pas
            if max(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)) > largeur \
                    or max(seg.dest.distance_to_droite(left_droite), seg.dest.distance_to_droite(right_droite)) > largeur:
                continue

            # Si c'est la balise(objet a trouver) on la recupere
            if isinstance(elem, Balise):
                self.balise = elem

            # On ajoute l'element dans la liste
            self.elements.append(elem)

    def get_distance(self, robot):
        """
        robot -> None

        Permet de calculer la distance à l'obstacle le plus proche du robot
        """

        largeur = robot.WHEEL_BASE_WIDTH

        # On recupere le vecteur de la droite  faciale du robot
        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        # On calcule l'angle de rotation du vecteur servo
        angle = vec_src.angle(vec_norme)

        # On calcule la nouvelle droite faciale du robot selon la rotation du servo
        # Et on calcule la nouvelle tete du robot
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

        # On parcours les element de la vision et on cherche la distance minimale entre les obstacle et le robot
        # # La distance entre le nouvelle tete et le point d'intersection entre la droite du servo et l'obstacle
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

        # Si la balse n'ent pas dans la vision alors on retourne directement les valeur par defaut
        if self.balise is None:
            return -1, -1

        vec_src = robot.vec_servo

        # On calcule la tete du robot
        milieu = Point.milieu(robot.chd, robot.cbd)

        # On calcule le milieu de la balise
        milieu_balise = Point.milieu(
            self.balise.segment.src, self.balise.segment.dest)

        # On cree le vecteur entre le milieu de la balise et la tete du robot
        vec_balise = Vecteur(milieu, milieu_balise)

        # On determine l'orientation ou elle est la balise (gauche ou droite)
        angle = vec_src.angle_sign(vec_balise)

        if angle >= 0:
            return angle, self.DROITE

        return -angle, self.GAUCHE
