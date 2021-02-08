from objet import Objet
from robotsimu import RobotSimu
from wall import Wall
from vision import Vision
from tool import *

class Simulation:

    #Constructeur
    def __init__(self, largeur, longueur, echelle, vision, taille_robot):
        # Crée la grille de simulation en fonction des parametres donnés avec l'échelle, le robot, la largeur et la longueur de la simulation
        self.larg = largeur * echelle.nb_cases
        self.long = longueur * echelle.nb_cases
        self.grille = create_grille(self.larg, self.long)
        self.__init_wall_grille__() #pose des robots sur les bornes de la grille
        self.vision = vision
        self.taille_robot = taille_robot
        #crée le robot de la simulation
        self.robot_simu = RobotSimu()
        self.init_robot()


      #crée le robot de la simulation
    def init_robot(self):
        self.__placer_robot__(int(self.larg / 2), int(self.long / 2), 0)


    #positionne des murs sur les limites du terrain
    def __init_wall_grille__(self):
        for i in range(len(self.grille)):
            self.grille[i][0] = Wall()
            self.grille[i][len(self.grille[0])-1] = Wall()

        for i in range(len(self.grille[0])):
            self.grille[0][i] = Wall()
            self.grille[len(self.grille)-1][i] = Wall()


    #avance le robot
    def forward(self, x, speed):

        # si le point de destination est hors grille on sort
        if x + self.robot_simu.posx >= len(self.grille[0]):
            print("cette distance est trop grande")
            return 

        # on syncronise la vision    
        self.sync_vision()

        # on verifie si le chemain est libre et qu'on peut avancer
        if not self.vision.libre_sur(x) :
            return

        # on calcule le vecteur de destination du robot (le vecteur qu'il va suivre)
        vectDir = get_vect_from_angle(self.robot_simu.direction)

        # on considere que le vecteur de base est le vecteur des abcisses
        vicSrc = (1,0)

        # on calcule l'angle avec le signe 
        angle = self.robot_simu.direction
        
        # on recupere les coordonnee du point de destination par rapport au robot
        xpos = cos(to_radian(angle)) * x
        ypos = sin(to_radian(angle)) * x
        print(cos(to_radian(180)))

        # on modifie les points de destination par rapport a la grille de la  simulation
        # if angle > 0:
        #     ypos = self.robotSimu.posy - ypos
        # else:
        ypos = self.robot_simu.posy + ypos
        
        # if abs(angle) > 90:
        #     xpos = self.robotSimu.posx - xpos
        # else:
        xpos += self.robot_simu.posx
        
        # on supprime le robot de la grille 
        self.__enlever_robot_map__()

        # on l'ajoute dans sa nouvelle position
        self.__placer_robot__(round(xpos),round(ypos),self.robot_simu.direction)

  
    def __placer_robot__(self,x,y,dir):
        self.robot_simu.set_pos(x, y, dir) #le pose en plein milieu du terrain
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robot_simu.posx - int(self.taille_robot/2) , self.robot_simu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robot_simu.posy - int(self.taille_robot/2) , self.robot_simu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = self.robot_simu
        
    
    def __enlever_robot_map__(self):
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robot_simu.posx - int(self.taille_robot/2) , self.robot_simu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robot_simu.posy - int(self.taille_robot/2) , self.robot_simu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = None


    # positionne le robot en direction de l'angle en parametre
    def tourne(self, angle):
        self.robot_simu.direction += angle


    def sync_vision(self):
        """
            Pemet de synchroniser la vision du robot selon sa position et son angle
        """
        grille = create_grille(self.larg, self.long)

        for i in range(self.vision.larg):
            for j in range(self.vision.long):
                self.vision.grille[i][j] = Wall()
        
        vec_src = get_vect_from_angle(self.robot_simu.direction)

        src_point = get_src_point(self.taille_robot, self.robot_simu.posx, self.robot_simu.posy, self.robot_simu.direction)

        droite_sep = (vec_src[0], vec_src[1], (- vec_src[0] * src_point[0] - vec_src[1] * src_point[1]))

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

        for i in range(len(self.grille[0])):
            for j in range(len(self.grille)):
                dest_point = (i, j)
                vec_dest = get_vect_from_points(src_point, dest_point)
               
                if src_point != dest_point and in_vision(vec_src, vec_dest) and 0 < distance(droite_sep, dest_point) <= self.vision.long and distance(droite_direction, dest_point) <= self.vision.larg//2:
                    
                    y = ceil(distance(droite_sep, dest_point))
                    y -= 1

                    x = floor(distance(droite_direction, dest_point))
  
                    if angle_sign(vec_src, vec_dest) <= 0:
                        x = self.vision.larg//2 + x
                    else:
                        x = self.vision.larg//2 - x

                    # Car axe robot inclus dedans
                    if x == 0:
                        continue

                    x -= 1

                    self.vision.grille[x][y] = self.grille[i][j]
                    grille[i][j] = self.grille[i][j]

        # affiche(self.vision.grille)
        # affiche(grille)