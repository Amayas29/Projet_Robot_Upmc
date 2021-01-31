from Objet import Objet
from RobotSimu import RobotSimu
from Wall import Wall
from Vision import Vision
from Static import Static

class Simulation:

    def __init__(self, largeur, longueur, echelle, vision, taille_robot):
        self.larg=largeur*echelle.nbCases
        self.long=longueur*echelle.nbCases
        self.grille = Static.createGrille(self.larg, self.long)
        self.vision = vision
        self.taille_robot = taille_robot
        self.robotSimu = RobotSimu()
        self.init_Robot()
        Static.affiche(self.grille)

        
    def init_Robot(self):
        self.robotSimu.setPos(int(self.larg / 2), int(self.long / 2), "N")
        pair = self.taille_robot % 2
        for i in range(self.robotSimu.posx - int(self.taille_robot/2) , self.robotSimu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robotSimu.posy - int(self.taille_robot/2) , self.robotSimu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = self.robotSimu
