from   time import sleep
import threading

class Controleur:

    def __init__(self, vision, robot, arene, fps):
        self.arene = arene
        self.vision = vision
        self.robot = robot
        self.fps = fps
        self.strategies = []
        self.current_strat = -1


    def add_startegie(self, strategie):
        self.strategies.append(strategie)

    
    def select_startegie(self, index):
        if index < 0 or index > len(self.strategies):
            return
        
        self.strategies[self.current_strat].start()
        self.current_strat = index


    def boucle(self): 
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):

        if self.current_strat == len(self.strategies):
            return

        if self.strategies[self.current_strat].is_stop():
            return

        self.vision.sync_vision(self.arene.elements, self.robot)
        self.strategies[self.current_strat].run(self.vision)