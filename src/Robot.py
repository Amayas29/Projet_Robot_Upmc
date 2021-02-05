from Vision import Vision
from Simulation import Simulation
from Echelle import Echelle
from Static import Static
from IRL import IRL
import threading
import time
from time import sleep

# Classe qui représente le Robot 
class Robot:
    
    # Constructeur
    def __init__(self, echelle):
        self.isSimu = False # attribut qui permet de savoir si on est dans une simulation on si on veut utiliser le robot irl
        # en % les speed
        self.speedL = 0
        self.speedR = 0
        # angle Tete: 0 centre, 90 gauche, 270 droite
        self.angleTete = 0
        self.batterie = 100
        self.echelle = Echelle(echelle) # initialise l'échelle avec celle donnée en parametre
        # le 0.25 est la taille du robot
        self.tailleRobot = int(self.echelle.nbCases * 0.25)
        self.vision = Vision(self.echelle.nbCases * 4,self.echelle.nbCases * 4, self.tailleRobot) # initialise la visiondu robot, représente ce qui apparait devant le robot
        self.irl = IRL()
        self.simu = None


    # methode qui permet de définir le mode du robot
    def setSimu(self, boole):
        """assuming boole is boolean""" 
        if boole:
            # si le parametre est True alors on souhaite etre en mode simulation
            print("Mode Simulation active")
            #on initialise la simulation
            self.isSimu = True
            self.simu = Simulation(5,1,self.echelle, self.vision, self.tailleRobot)
        else:
            #sinon on parametre le robot pour l'utiliser irl
            print("Mode IRL active")
            self.isSimu = False
            self.simu = None

    # deplace, si possible, le robot sur une distance x avec une vitesse speed et un angle (angle)
    def deplaceRobot(self, x, speed, angle):
        """ speed : 0 a 100 , angle: angle de rotation par rapport a l'etat actuel (0 n'est donc pas forcement le Nord), x : uniter de distance"""
        #on cherche à savoir en quel mode est le robot
        if self.isSimu:
            #mode simulation
            if angle != 0:
                #on tourne le robot d'un certain angle
                self.simu.tourne(angle)
            if self.vision.libresur(x):
                #si il peut aller sur x distance
                self.simu.forward(x, speed)
                print("fait!")
                return
            else:
                #sinon c'est qu'il y a un obstacle
                print("Le robot est bloquer")
                return                
        else:
            #mode irl, meme processus que pour le mode simulation mais avec de vraies méthodes
            if angle != 0:
                #50% de vitesse sur la rotation pour être moins brutal
                self.irl.tourne(angle, 50)
                # 3 secondes suffisent à faire 360°
                time.sleep(3)
            if self.vision.libresur(x):
                self.irl.forward(x, speed)
                print("fait!")
                return
            else:
                print("Le robot est bloquer")
                return   



if __name__ == '__main__':
    rob = Robot(9)
    rob.setSimu(True)
