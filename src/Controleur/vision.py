from Utils.tools import Point, Segment, Droite, Vecteur

class Vision:

    def __init__(self, largeur, distance):
        
        self.largeur = largeur
        self.distance = distance
        self.elements = []
    

    def sync_vision(self, elements, robot):
        """
            Permet de synchroniser la vision du robot selon sa position et son angle
        """
        self.vision.elements = []

        vec_src = Vecteur.get_vect_from_angle(robot.angle)

        src_point = Point.milieu(robot.chd, robot.cbd) 

        droite_sep = Droite.get_droite(vec_src, src_point)

        if droite_sep.b == 0:
            new_point = Point(src_point.x,  src_point.y + 1)
        
        else:
            x = 0
            if x == src_point.x:
                x += 1
         
            y = (- droite_sep.a * x - droite_sep.b) / droite_sep.b
            new_point = Point(x, y)

        vec_unit = Vecteur(src_point, new_point)
        droite_direction = Droite.get_droite(vec_unit, src_point)

        for elt in self.elements:

                dest_point = Point(elt.posx, elt.posy)
              
                vec_dest = Vecteur(src_point, dest_point)

                if src_point != dest_point and vec_src.angle(vec_dest) <= 90 and 0 < dest_point.distance_to_droite(droite_sep) <= self.vision.long and dest_point.distance_to_droite(droite_direction) <= self.vision.larg//2:
                    self.vision.elements.append(elt)
    

    def check_collisions(self, robot):
        return False

    