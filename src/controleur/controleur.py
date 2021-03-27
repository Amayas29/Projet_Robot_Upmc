from time import sleep
import threading


class Controleur:

    def __init__(self, arene):
        self.arene = arene
        self.vision = arene.robot.vision
        self.robot = arene.robot
        self.strategies = []
        self.current_strat = -1

    def add_startegie(self, strategie):
        self.strategies.append(strategie)

    def select_startegie(self, index):
        if index < 0 or index > len(self.strategies):
            return

        self.strategies[self.current_strat].start()
        self.current_strat = index

    def boucle(self, fps):
        while True:
            self.update()
            sleep(1./fps)

    def update(self):

        if self.current_strat == len(self.strategies):
            return

        if self.strategies[self.current_strat].is_stop:
            return

        self.vision.sync_vision(self.robot, self.arene.elements)
        self.strategies[self.current_strat].run()
