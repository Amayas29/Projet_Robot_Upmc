from Vision import Vision
from Simulation import Simulation
from Echelle import Echelle
from Static import Static
from IRL import IRL
import threading
import time
from time import sleep


class Robot:
    
    def __init__(self, echelle):
        self.isSimu = False
        # en % les speed
        self.speedL = 0
        self.speedR = 0
        # angle Tete: 0 centre, 90 gauche, 270 droite
        self.angleTete = 0
        self.batterie = 100
        self.echelle = Echelle(echelle)
        # le 0.25 est la taille du robot
        self.tailleRobot = int(self.echelle.nbCases * 0.25)
        self.vision = Vision(self.echelle.nbCases * 4,self.echelle.nbCases * 4, self.tailleRobot)
        self.irl = IRL()
        self.simu = None


    def setSimu(self, boole):
        """assuming boole is boolean""" 
        if boole:
            print("Mode Simulation active")
            self.isSimu = True
            self.simu = Simulation(5,1,self.echelle, self.vision, self.tailleRobot)
        else:
            print("Mode IRL active")
            self.isSimu = False
            self.simu = None


    def deplaceRobot(self, x, speed, angle):
        """ speed : 0 a 100 , angle: angle de rotation par rapport a l'etat actuel (0 n'est donc pas forcement le Nord), x : uniter de distance"""
        if self.isSimu:
            if angle != 0:
                self.simu.tourne(angle)
            if self.vision.libresur(x):
                self.simu.forward(x, speed)
                print("fait!")
                return
            else:
                print("Le robot est bloquer")
                return                
        else:
            if angle != 0:
                #50% de vitesse sur la rotation pour être moin brutal
                self.irl.tourne(angle, 50)
                # 3 seconde suffise a faire 360°
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
