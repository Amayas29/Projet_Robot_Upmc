from Objet import Objet
from RobotSimu import RobotSimu
from Wall import Wall
from Vision import Vision
from Tool import *

class Simulation:

    #Constructeur
    def __init__(self, largeur, longueur, echelle, vision, taille_robot):
        # Crée la grille de simulation en fonction des parametres donnés avec l'échelle, le robot, la largeur et la longueur de la simulation
        self.larg = largeur*echelle.nbCases
        self.long = longueur*echelle.nbCases
        self.grille = createGrille(self.larg, self.long)
        self.__init_wall_grille() #pose des robots sur les bornes de la grille
        self.vision = vision
        self.taille_robot = taille_robot
        #crée le robot de la simulation
        self.robotSimu = RobotSimu()
        self.init_Robot()
        affiche(self.grille)

    #crée le robot de la simulation
    def init_Robot(self):
        self.robotSimu.setPos(int(self.larg / 2), int(self.long / 2), 0) #le pose en plein milieu du terrain
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robotSimu.posx - int(self.taille_robot/2) , self.robotSimu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robotSimu.posy - int(self.taille_robot/2) , self.robotSimu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = self.robotSimu

    #positionne des murs sur les limites du terrain
    def __init_wall_grille(self):
    	for i in range(len(self.grille)):
    		self.grille[i][0] = Wall()
    		self.grille[i][len(self.grille[0])-1] = Wall()

    	for i in range(len(self.grille[0])):
    		self.grille[0][i] = Wall()
    		self.grille[len(self.grille)-1][i] = Wall()

    #avance le robot
    def forward(self, x, speed):
        return True


    def tourne(self, angle):
        return