from   time import sleep
import threading

class Controleur:

    def __init__(self, vision, robot, fps):
        self.vision = vision
        self.robot = robot
        self.fps = fps
    

    def forward(self, vitesse):
        if self.vision.check_collisions(self.robot):
            return
      
        self.robot.start(vitesse)
        
        while True:
            if self.vision.check_collisions(self.robot):
                break

            sleep(1./self.fps)
        
        self.robot.stop()


    def forward2(self):
        while True:
        
            if self.vision.check_collisions(self.robot):
                break
            else:
                self.robot.start()
            
            sleep(1./self.fps)
            self.robot.stop()

