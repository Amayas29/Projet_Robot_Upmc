from   time import sleep
import threading

class Modele:

    def __init__(self, fps):
        self.fps = fps

    
    def update_modele(self):

        while True:
            sleep(1./self.fps)