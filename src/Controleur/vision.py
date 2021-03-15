from Utils.tools import Point, Droite, Vecteur
from Modele.robot import Robot
from robot2I013.robot2I013 import Robot2I013

class Vision:

    def __init__(self, distance):
        self.distance = distance
        self.elements = []
    

    def sync_vision(self, robot, elements=[]):
        """
            Permet de synchroniser la vision du robot selon sa position et son angle
        """
        if (isinstance(robot, Robot)):
            self.sync_vision_simu(robot, elements)
        elif (isinstance(robot, Robot2I013)):
            self.sync_vision_irl(robot)
        else:
            exit(1)
    

    def check_collisions(self):
        return self.elements != []
        

    def sync_vision_simu(self, robot, elements):
        
        self.vision.elements = []

        milieu = Point.milieu(robot.chd, robot.cbd)
        largeur = robot.chb - robot.cbd

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = Vecteur.get_vect_from_angle(robot.angle)

        left_droite  = Droite.get_droite(vec_norme, robot.chd)
        right_droite = Droite.get_droite(vec_norme, robot.cbd)

        front_droite = Droite.get_droite(  vec_src, robot.cbd)

        for elem in elements:

            seg = elem.segment
            new_vec_src = Vecteur(milieu, seg.src)
            new_vec_dest = Vecteur(milieu, seg.dest)

            if vec_src.angle(new_vec_src) > 90 and vec_src.angle(new_vec_dest) > 90:
                continue

            if min(seg.src.distance_to_droite(front_droite), seg.dest.distance_to_droite(front_droite)) > self.distance:
                continue

            if not seg.intersection(robot.chd, vec_norme) and not seg.intersection(robot.cbd, vec_norme):
                continue

            if max(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)) > largeur:
                continue

            self.vision.elements(elem)


    def sync_vision_irl(self, robot):
        self.vision.elements = []