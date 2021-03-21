from   time import sleep
import threading
from Utils.tools import Vecteur

class Modele:

    def __init__(self, fps):
        self.fps = fps

    
    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
        pass
            

        
    def forward(self):
        """
        Permet de bouger le robot d'une case en suivant ca direction
        """
        
        angle = self.angle % 360
        vict = Vecteur.get_vect_from_angle(angle)
       
        self.chg += vict.vict
        self.chd += vict.vict
        self.cbg += vict.vict
        self.cbd += vict.vict
        self.center += vict.vict
        
        
    def start(self, vitesse):
        pass
    
    def stop(self):
        pass

    
    def tourne(self, angle):
        """
        Permet de tourner le robot 
        """
        angle = angle % 360
        self.angle = angle
        self.chg.rotation(self.center, angle)
        self.chd.rotation(self.center,angle)
        self.cbg.rotation(self.center,angle)
        self.cbd.rotation(self.center,angle)
      