from vision import Vision
from simulation import Simulation
from echelle import Echelle
from tool import *
from irl import IRL
import threading
import time
from time import sleep

# Classe qui représente le Robot 
class Robot:
    
    # Constructeur
    def __init__(self, echelle):
        self.is_simu = False # attribut qui permet de savoir si on est dans une simulation on si on veut utiliser le robot irl
        # en % les speed
        self.speed_l = 0
        self.speed_r = 0
        # angle Tete: 0 centre, 90 gauche, 270 droite
        self.angle_tete = 0
        self.batterie = 100
        self.echelle = Echelle(echelle) # initialise l'échelle avec celle donnée en parametre
        # le 0.25 est la taille du robot
        self.taille_robot = int(self.echelle.nb_cases * 0.25)
        self.vision = Vision(self.echelle.nb_cases * 4,self.echelle.nb_cases * 4, self.taille_robot) # initialise la visiondu robot, représente ce qui apparait devant le robot
        self.irl = IRL()
        self.simu = None


    # methode qui permet de définir le mode du robot
    def set_simu(self, boole):
        """assuming boole is boolean""" 
        if boole:
            # si le parametre est True alors on souhaite etre en mode simulation
            print("Mode Simulation active")
            #on initialise la simulation
            self.is_simu = True
            self.simu = Simulation(4, 4,self.echelle, self.vision, self.taille_robot)
        else:
            #sinon on parametre le robot pour l'utiliser irl
            print("Mode IRL active")
            self.is_simu = False
            self.simu = None


    # deplace, si possible, le robot sur une distance x avec une vitesse speed et un angle (angle)
    def deplace_robot(self, x, speed, angle):
        """ speed : 0 a 100 , angle: angle de rotation par rapport a l'etat actuel (0 n'est donc pas forcement le Nord), x : uniter de distance"""
        #on cherche à savoir en quel mode est le robot
        if self.is_simu:
            #mode simulation
            if angle != 0:
                #on tourne le robot d'un certain angle
                self.simu.tourne(angle)
            
            #si il peut aller sur x distance
            return self.simu.forward(x, speed)

        else:
            #mode irl, meme processus que pour le mode simulation mais avec de vraies méthodes
            if angle != 0:
                #50% de vitesse sur la rotation pour être moins brutal
                self.irl.tourne(angle, 50)
                # 3 secondes suffisent à faire 360°
                time.sleep(3)
            if self.vision.libre_sur(x):
                self.irl.forward(x, speed)
                print("fait!")
                return True
            else:
                print("Le robot est bloquer")
                return False  