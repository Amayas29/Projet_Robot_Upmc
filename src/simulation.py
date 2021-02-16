from objet import Objet
from robotsimu import RobotSimu
from wall import Wall
from vision import Vision
from tool import *
import time
from time import sleep

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
        """
            initialiser le robot et le mettre au centre de la map
        """
        self.__placer_robot__(int(self.larg / 2), int(self.long / 2), 0)


    #positionne des murs sur les limites du terrain
    def __init_wall_grille__(self):
        """
            initialiser les murs de la grille
        """
        for i in range(len(self.grille)):
            add_objet(self.grille, Wall(), i, 0)
            add_objet(self.grille, Wall(), i, len(self.grille[0])-1)

        for i in range(len(self.grille[0])):
            add_objet(self.grille, Wall(), 0, i)
            add_objet(self.grille, Wall(), len(self.grille)-1, i)
 


    def __forward__(self,point_src,speed):
        """
            permet de bouger le robot d'une case en suivant ca direction
        """
        
        # syncroniser la vision     
        self.sync_vision()

        # verifier si y a aucun objet (si rien ne nous stop pour avancer)
        if not self.vision.libre_sur(1, self.taille_robot, self.robot_simu.direction, self.robot_simu.posx, self.robot_simu.posy):
            return (-1,-1)

        # normaliser l'angle et calculer le vecteur de direction
        angle = normalise_angle(self.robot_simu.direction)
        vict = get_vect_from_angle(angle)
       
        # calculer la nouvelle position du robot dans la grille
        x = point_src[0]+vict[0] * speed
        y = point_src[1]+vict[1] * speed
        point_src = (x,y)
    
        sleep(0.1)
            
        # on supprime le robot de la map et on l'ajoute dans sa nouvelle position
        self.__enlever_robot_map__()
        self.__placer_robot__(round(point_src[0]),round(point_src[1]),self.robot_simu.direction)

        # on affiche la grille
        affiche(self.grille)
            
        #on return true si tout se passe bien 
        return point_src
        
        

    def forward(self, x, speed):
        """
            permet d'avancer le robot de x case dans ca direction
        """
        if speed == 0:
            return
        point = 0

        point_src=(self.robot_simu.posx,self.robot_simu.posy)
        x = (x//speed)+(x % 2)
        while  x > 0:
            print("hem",x)
            point_src = self.__forward__(point_src,speed)
            if  point_src == (-1,-1):
                print("deplacement impossible un objet est detecter")
                return False
            
            
            x -= 1
        

    def __placer_robot__(self,x,y,dir):
        """
            permet de placer le robot sur la grille
        """
        self.robot_simu.set_pos(x, y, dir) #le pose en plein milieu du terrain
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robot_simu.posx - int(self.taille_robot/2) , self.robot_simu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robot_simu.posy - int(self.taille_robot/2) , self.robot_simu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = self.robot_simu
        
    
    def __enlever_robot_map__(self):
        """
            permet d'enlever le robot de la grille
        """
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robot_simu.posx - int(self.taille_robot/2) , self.robot_simu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robot_simu.posy - int(self.taille_robot/2) , self.robot_simu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = None


    # positionne le robot en direction de l'angle en parametre
    def tourne(self, angle):
        """
            permet de tourner le robot 
        """
        angle = normalise_angle(angle)
        self.robot_simu.direction += angle
        return 1
        # for i in range(len(self.grille)):
        #     for j in range(len(self.grille[0])):
        #         if isinstance(self.grille[i][j], RobotSimu):
        #             rob = self.grille[i][j]
        #             ip, jp = tourne(rob.posx, rob.posy, angle)
        #             self.grille[i][j] = None
        #             add_objet(self.grille, rob, ip, jp)

    def sync_vision(self):
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
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):

                if self.grille[i][j] == None:
                    continue

                dest_point = (self.grille[i][j].posx, self.grille[i][j].posy)
              
                vec_dest = get_vect_from_points(src_point, dest_point)

                if src_point != dest_point and in_vision(vec_src, vec_dest) and 0 < distance(droite_sep, dest_point) <= self.vision.long and distance(droite_direction, dest_point) <= self.vision.larg//2:
                    self.vision.elements.append(self.grille[i][j])