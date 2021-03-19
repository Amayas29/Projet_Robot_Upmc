from   time import sleep
import threading
from Utils.tools import Vecteur
from Controleur.vision import Vision


class Modele:

    def __init__(self, fps, arene, angle):
        self.fps = fps
        self.angle = angle
        self.arene = arene
        self.robot = arene.robot
    
    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
        # syncroniser la vision     
        Vision.sync_vision(self.robot,[])
        
        if Vision.check_collisions():
            self.stop()

        self.start(vitesse=2)

        if self.angle != 0:
            self.tourne(self.angle)
            self.forward()
            

    def forward(self):
        """
        Permet de bouger le robot d'une case en suivant ca direction
        """

        # normaliser l'angle et calculer le vecteur de direction
        angle1 = self.angle % 360
        vict = Vecteur.get_vect_from_angle(angle1)
        self.robot.vec_deplacement = vict
       
        self.robot.chg += self.robot.vec_deplacement.vect
        self.robot.chd += self.robot.vec_deplacement.vect
        self.robot.cbg += self.robot.vec_deplacement.vect
        self.robot.cbd += self.robot.vec_deplacement.vect
        self.robot.center += self.robot.vec_deplacement.vect
    

    def start(self, vitesse):
        self.robot.lspeed = vitesse
        self.robot.rspeed = vitesse
    
    def stop(self):
        self.robot.lspeed = 0
        self.robot.rspeed = 0

    
    def tourne(self, angle):
        """
        Permet de tourner le robot 
        """

        self.angle = angle % 360
        
        self.robot.chg.rotation(self.robot.center, angle)
        self.robot.chd.rotation(self.robot.center,angle)
        self.robot.cbg.rotation(self.robot.center,angle)
        self.robot.cbd.rotation(self.robot.center,angle)
      