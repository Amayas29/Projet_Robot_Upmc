from Vision import Vision
from Simulation import Simulation
from Echelle import Echelle
from Static import Static

class Robot:
    
    def __init__(self, echelle):
        self.isSimu = False
        # en % les speed
        self.speedL = 0
        self.speedR = 0
        # angle Tete: 90 centre, 0 gauche, 180 droite
        self.angleTete = 90
        self.batterie = 100
        self.echelle = Echelle(echelle)
        # le 0.25 est la taille du robot
        self.tailleRobot = int(self.echelle.nbCases * 0.25)
        self.vision = Vision(self.echelle.nbCases * 4,self.echelle.nbCases * 4)
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


    def deplaceRobot(self, x, speed):
        if isSimu:
            return
        else:
            return


if __name__ == '__main__':
    rob = Robot(9)
    rob.setSimu(True)
