from tool import is_occupe, normalise_angle, get_src_point, collision, get_vect_from_angle, get_vect_from_points, distance
from robotsimu import RobotSimu
from math import sqrt

#représente la vision du robot, ce qu'il voit devant lui
class Vision:

    #Constructeur
    def __init__(self, larg, long):
        #crée une mini grille,copiant sur celle de simulation
        self.elements = []
        self.larg = larg
        self.long = long

    #Determine si sur une distance donnee, il y a des obstacles ou non
    def libre_sur(self, dist, taille_robot, angle, posx, posy):

        #verifie si le parametre est cohérent
        if(dist > self.larg):
            print("Vision impossible !")
            return False
        
        angle = normalise_angle(angle)

        vec_src = get_vect_from_angle(angle) # prend la direction du robot

        src_point = get_src_point(taille_robot, posx, posy, angle) 

        droite_sep = (vec_src[0], vec_src[1], (- vec_src[0] * src_point[0] - vec_src[1] * src_point[1])) #pour découper avec les droites la vision cherchée

        if droite_sep[1] == 0:
            new_point = ( src_point[0],  src_point[1] + 1)
        
        else:
            x = 0
            if x == src_point[0]:
                x += 1
         
            y = (- droite_sep[0] * x - droite_sep[2]) / droite_sep[1]
            new_point = (x, y)

        vec_unit = get_vect_from_points(src_point, new_point)
        droite_direction = (vec_unit[0], vec_unit[1], (- vec_unit[0] * src_point[0] - vec_unit[1] * src_point[1]))

        if not (angle == 0 or angle == 90 or angle == 180 or angle == 270):
            taille_robot = round(sqrt(2) * taille_robot)
        
        for objet in self.elements:
           
           if objet.posx == 39 and objet.posy == 41:
               print(distance(droite_sep, (objet.posx, objet.posy)))

           if distance(droite_sep, (objet.posx, objet.posy)) <= dist and collision(objet, droite_direction, taille_robot):
                return False
            
        return True


    def distance_max_obstacle(self):
        #return la distance max avant le premier obstacle rencontrer (en prenant en compte la largeur du robot)
        return 1
