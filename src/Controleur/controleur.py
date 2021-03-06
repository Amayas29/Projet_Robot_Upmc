from   time import sleep
import threading

class Controleur:

    def __init__(self, vision, robot, fps):
        self.vision = vision
        self.robot = robot
        self.fps = fps
    

    def forward(self, vitesse, temps):
        if self.vision.check_collisions(self.robot):
            return
      
        self.robot.start(vitesse)
        
        sec = 0
        while sec < temps :
            
            if self.vision.check_collisions(self.robot):
                break

            sleep(1./self.fps)
            sec += 1./self.fps

        self.robot.stop()


    def forward2(self):
        while True:
        
            if self.vision.check_collisions(self.robot):
                break
            else:
                self.robot.start()
            
            sleep(1./self.fps)
            self.robot.stop()

