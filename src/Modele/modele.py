from time import sleep
import threading
from datetime import datetime
from Utils.tools import Vecteur, Point
from .vision import Vision
from math import cos, sin, PI


class Modele:

    def __init__(self, fps, arene):
        self.fps = fps
        self.arene = arene
        self.robot = arene.robot
        self.temps_precedent = datetime.now()
    
    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
        # syncroniser la vision     
        Vision.sync_vision(self.robot,[])
        
        if Vision.check_collisions():
            self.stop()

        self.forward()
        self.start()
            

    def forward(self):
        """
        Permet de bouger le robot d'une case en suivant ca direction
        """
        diff_temps = (datetime.now() - self.temps_precedent).total_seconds()
        if self.robot.lspeed == self.robot.rspeed :
            angle_roue =  diff_temps * self.robot.lspeed
           
            distance = angle_roue * (PI * self.robot.WHEEL_DIAMETER / 360)
            
            self.robot.posr += angle_roue 
            self.robot.posl += angle_roue
            
            point_tmp = Point(self.robot.vec_deplacement.vect[0] + distance, self.robot.vec_deplacement.vect[1] + distance)
            
            self.chg += point_tmp
            self.cbg += point_tmp
            self.chd += point_tmp
            self.cbd += point_tmp

        elif  self.robot.lspeed == 0 and self.robot.rspeed != 0:
            roue = Point((self.robot.chg.x + self.robot.chd.x)/2 , (self.robot.chg.y + self.robot.chd.y)/2)
            angle_roue = diff_temps * self.robot.rspeed
            distance = angle_roue * (PI * self.robot.WHEEL_DIAMETER / 360)
          
            self.robot.posr += angle_roue

            angle = distance/((PI * self.robot.chd - self.robot.cbd)/180)
            self.robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)
            self.chg.rotate(angle, roue)
            self.cbg.rotate(angle, roue)
            self.chd.rotate(angle, roue)
            self.cbd.rotate(angle, roue)

        elif self.robot.rspeed == 0 and self.robot.lspeed != 0 :
            roue = Point((self.robot.cbg.x + self.robot.cbd.x)/2 , (self.robot.cbg.y + self.robot.cbd.y)/2)
        
            angle_roue = diff_temps * self.robot.lspeed
            distance = angle_roue * (PI * self.robot.WHEEL_DIAMETER / 360)
            
            self.robot.posl += angle_roue
           
            angle = distance/((PI * self.robot.chd - self.robot.cbd)/180)
            self.robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)

            self.chg.rotate(angle, roue)
            self.cbg.rotate(angle, roue)
            self.chd.rotate(angle, roue)
            self.cbd.rotate(angle, roue)

        #TODO
        elif self.robot.lspeed > self.robot.rspeed:
            pass
        elif self.robot.lspeed < self.robot.rspeed:
            pass
        else:
            pass
        
        
    

    def start(self):
        self.temps_precedent = datetime.now()
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT , 0)
    
    def stop(self):
        self.robot.lspeed = 0
        self.robot.rspeed = 0

    