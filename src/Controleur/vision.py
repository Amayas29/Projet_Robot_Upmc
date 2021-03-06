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

        vec_src = get_vect_from_angle(self.robot_simu.direction) # prend la direction du robot

        src_point = get_src_point(self.taille_robot, self.robot_simu.posx, self.robot_simu.posy, self.robot_simu.direction) 

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

        #construction de la vision en fonction de sa destination et son angle
        #redécoupe la simulation pour en tiré une vision en fonction des paramètres du robot
        #on utilise des vecteurs
        # for i in range(len(self.grille)):
        #     for j in range(len(self.grille[0])):

        for elt in self.elements:

                # if self.grille[i][j] == None:
                #     continue

                dest_point = (elt.posx, elt.posy)
              
                vec_dest = get_vect_from_points(src_point, dest_point)

                if src_point != dest_point and in_vision(vec_src, vec_dest) and 0 < distance(droite_sep, dest_point) <= self.vision.long and distance(droite_direction, dest_point) <= self.vision.larg//2:
                    # self.vision.elements.append(self.grille[i][j])
                    self.vision.elements.append(elt)
    

    def check_collisions(self, robot):
        return False

    #def check_collisions(self, objet, droite_dir, taille):
    #  taille = max(1, taille//2)
    #  return distance(droite_dir, (objet.posx, objet.posy)) <= taille

    