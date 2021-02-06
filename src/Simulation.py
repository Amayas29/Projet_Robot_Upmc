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
        dist=abs( x - self.robotSimu.poxs ) # dist = nombre de cases séparants le robot de x
        for i in range( dist ):
            # boucle pour etre plus réaliste
            x1 = self.robotSimu.posx + 1 # posx augmente ( position x du robot )
            y1 = self.robotSimu.posy
            grille[ self.robotSimu.posx ][ self.robotSimu.posy ] = None # vide l'ancienne position du robot
            grille[ x1 ][ y1 ] # met le robot sur sa nouvelle posx
            affiche( self.grille ) # affiche la simu à chaque avancement


    # positionne le robot en direction de l'angle en parametre
    def tourne(self, angle):
        self.robotSimu.dirrection = angle


    def syncVision(self):
        # Temp car pas encore fait de lien vers vision
        grille = createGrille(self.larg, self.long)

        vecSrc = getVectDirFromAngle(self.robotSimu.direction)
        # TODO determiner the extremite
        # srcPoint = extrimite(self.robotSimu)
        srcPoint = (self.robotSimu.posx, self.robotSimu.posy)

        droiteSep = (vecSrc[0], vecSrc[1], (- vecSrc[0] * srcPoint[0] - vecSrc[1] * srcPoint[1]))

        x = 0
        if x == srcPoint[0]:
            x += 1
        
        y = 0
        if droiteSep[1] != 0:
            y = (- droiteSep[0] * x - droiteSep[2]) / droiteSep[1]

        newPoint = (x, y)
        vecUnit = getVectDirFromPoints(srcPoint, newPoint)
        droiteDirection = (vecUnit[0], vecUnit[1], (- vecUnit[0] * srcPoint[0] - vecUnit[1] * srcPoint[1]))

        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                destPoint = (i, j)
                if inVision(vecSrc, getVectDirFromPoints(srcPoint, destPoint)) and distance(droiteSep, destPoint) <= self.vision.larg and distance(droiteDirection, destPoint) <= self.vision.long//2:
                    # TODO ajouter dans vision 
                    grille[i][j] = self.grille[i][j]

        affiche(grille)