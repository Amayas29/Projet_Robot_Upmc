from   time import sleep
import threading


class Affichage:

    def __init__(self, fps):
        self.fps = fps
        pass


    def update_affichage(self):

        while True:
            sleep(1./self.fps)