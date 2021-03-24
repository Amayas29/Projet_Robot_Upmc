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
        
        largeur = robot.chb - robot.cbd

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd
        
        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)
        
        left_droite  = Droite.get_droite(vec_norme, a)
        right_droite = Droite.get_droite(vec_norme, b)
        front_droite = Droite.get_droite(vec_src, milieu)

        for elem in elements:

            seg = elem.segment
            new_vec_src = Vecteur(milieu, seg.src)
            new_vec_dest = Vecteur(milieu, seg.dest)

            if vec_src.angle(new_vec_src) > 90 and vec_src.angle(new_vec_dest) > 90:
                continue

            if min(seg.src.distance_to_droite(front_droite), seg.dest.distance_to_droite(front_droite)) > self.distance:
                continue
         
            if min(min(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)),
            min(seg.dest.distance_to_droite(left_droite), seg.dest.distance_to_droite(right_droite))) > largeur:
                continue
            
            if not seg.intersection(a, vec_norme) and not seg.intersection(b, vec_norme):
                if max(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)) > largeur:
                    continue

            self.elements.append(elem)


    def sync_vision_irl(self, robot):
        self.elements = []


    def get_distance(self, robot):
        if (isinstance(robot, Robot)):
            self.get_distance_simu(robot)
        elif (isinstance(robot, Robot2I013)):
            self.get_distance_irl(robot)
        else:
            exit(1)
    

    def get_distance_simu(self, robot):
        
        largeur = robot.chb - robot.cbd

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd
        
        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)
        
        left_droite  = Droite.get_droite(vec_norme, a)
        right_droite = Droite.get_droite(vec_norme, b)
        front_droite = Droite.get_droite(vec_src, milieu)
        
        mini = 0
        for elem in self.elements:
            seg = elem.segment
            mini  = min(seg.src.distance_to_droite(front_droite), mini, seg.dest.distance_to_droite(front_droite))
                
        return mini


    def get_distance_irl(self, robot):
        pass