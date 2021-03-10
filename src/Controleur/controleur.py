from   time import sleep
import threading

class Controleur:

    def __init__(self, vision, robot, arene, fps):
        self.arene = arene
        self.vision = vision
        self.robot = robot
        self.fps = fps
        self.strategies = []
        self.current_start = -1


    def add_startegie(self, strategie):
        self.strategies.append(strategie)

    
    def select_startegie(self, index):
        if index < 0 or index > len(self.strategies)
            return
        
        self.strategies[self.current_start].start()
        self.current_start = index


    def boucle(self): 
        self.robot.start()
        while True:
            self.updade()
            sleep(1./self.fps)


    def update(self):

        if self.current_start == len(self.strategies):
            return

        if self.strategies[self.current_start].is_stop():
            return

        self.vision.sync_vision(self.arene.elements, self.robot)
        self.strategies[self.current_start].run()

"""
strat = [avance, tourne, avance, tourne, avance, tourne, avance, tourne]
"""
""""
    def updade(self, vitesse, temps):
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

"""