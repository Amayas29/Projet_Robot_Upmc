from   time import sleep
import threading


class Affichage:

    def __init__(self, arene, fps):
        self.fps = fps
        self.arene = arene
        pass


    def update_affichage(self):

        while True:
            sleep(1./self.fps)