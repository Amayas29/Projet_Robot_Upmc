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
        self.__init_wall_grille__() #pose des robots sur les bornes de la grille
        self.vision = vision
        self.taille_robot = taille_robot
        #crée le robot de la simulation
        self.robotSimu = RobotSimu()
        self.init_Robot()
        affiche(self.grille)


      #crée le robot de la simulation
    def init_Robot(self):
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
        if x + RobotSimu.posx >= len(self.grille[0]):
            print("cette distance est trop grande")
            return 

        # on syncronise la vision    
        self.syncVision()

        # on verifie si le chemain est libre et qu'on peut avancer
        if not self.vision.libresur(x) :
            return

        # on calcule le vecteur de destination du robot (le vecteur qu'il va suivre)
        vectDir = getVectDirFromAngle(self.robotSimu.direction)

        # on considere que le vecteur de base est le vecteur des abcisses
        vicSrc = (0,1)

        # on calcule l'angle avec le signe 
        angle = angle_sign(vicSrc,vectDir)
        
        # on recupere les coordonnee du point de destination par rapport au robot
        xpos = cos(angle) * x
        ypos = sin(angle) * x

        # on modifie les points de destination par rapport a la grille de la  simulation
        if angle > 0:
            ypos = RobotSimu.posy - ypos
        else:
            ypos = RobotSimu.posy + ypos
        
        if abs(angle) > 90:
            xpos = RobotSimu.posx - xpos
        else:
            xpos += RobotSimu.posx
        
        # on supprime le robot de la grille 
        self.__enlever_robot_map__()


        # on l'ajoute dans sa nouvelle position
        self.__placer_robot__(xpos,ypos,RobotSimu.direction)

  
  
  
    def __placer_robot__(self,x,y,dir):
        self.robotSimu.setPos(x, y, dir) #le pose en plein milieu du terrain
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robotSimu.posx - int(self.taille_robot/2) , self.robotSimu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robotSimu.posy - int(self.taille_robot/2) , self.robotSimu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = self.robotSimu
        
    
    def __enlever_robot_map__(self):
        pair = self.taille_robot % 2
        # pose le robot sur certaines cases en fonction de l'échelle et sa taille
        for i in range(self.robotSimu.posx - int(self.taille_robot/2) , self.robotSimu.posx + int(self.taille_robot/2) + pair):
            for j in range( self.robotSimu.posy - int(self.taille_robot/2) , self.robotSimu.posy + int(self.taille_robot/2) + pair):
                self.grille[i][j] = None
        return



    # positionne le robot en direction de l'angle en parametre
    def tourne(self, angle):
        self.robotSimu.direction += angle




    def syncVision(self):
        """
            Pemet de synchroniser la vision du robot selon sa position et son angle
        """
        grille = createGrille(self.larg, self.long)

        for i in range(self.vision.larg):
            for j in range(self.vision.long):
                self.vision.grille[i][j] = Wall()
        
        vecSrc = getVectDirFromAngle(self.robotSimu.direction)

        srcPoint = getSrcPoint(self.taille_robot, self.robotSimu.posx, self.robotSimu.posy, self.robotSimu.direction)
        print(srcPoint)

        droiteSep = (vecSrc[0], vecSrc[1], (- vecSrc[0] * srcPoint[0] - vecSrc[1] * srcPoint[1]))

        if droiteSep[1] == 0:
            newPoint = ( srcPoint[0],  srcPoint[1] + 1)
        
        else:
            x = 0
            if x == srcPoint[0]:
                x += 1
         
            y = (- droiteSep[0] * x - droiteSep[2]) / droiteSep[1]
            newPoint = (x, y)

        vecUnit = getVectDirFromPoints(srcPoint, newPoint)
        droiteDirection = (vecUnit[0], vecUnit[1], (- vecUnit[0] * srcPoint[0] - vecUnit[1] * srcPoint[1]))

        for i in range(len(self.grille[0])):
            for j in range(len(self.grille)):
                destPoint = (i, j)
                vecDest = getVectDirFromPoints(srcPoint, destPoint)
               
                if srcPoint != destPoint and inVision(vecSrc, vecDest) and 0 < distance(droiteSep, destPoint) <= self.vision.long and distance(droiteDirection, destPoint) <= self.vision.larg//2:
                    
                    y = ceil(distance(droiteSep, destPoint))
                    y -= 1

                    x = floor(distance(droiteDirection, destPoint))
  
                    if angle_sign(vecSrc, vecDest) <= 0:
                        x = self.vision.larg//2 + x
                    else:
                        x = self.vision.larg//2 - x

                    # Car axe robot inclus dedans
                    if x == 0:
                        continue

                    x -= 1
                
                    # if (str(self.grille[i][j]).endswith("9")):
                    #     print(self.grille[i][j], x, y, i, j, distance(droiteDirection, destPoint), distance(droiteSep, destPoint), angle_sign(vecSrc, vecDest), self.vision.larg//2)
                    
                    self.vision.grille[x][y] = self.grille[i][j]
                    grille[i][j] = self.grille[i][j]

        affiche(self.vision.grille)
        affiche(grille)