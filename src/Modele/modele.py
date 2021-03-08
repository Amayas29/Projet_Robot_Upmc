from   time import sleep
import threading

class Modele:

    def __init__(self, fps):
        self.fps = fps

    
    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
        pass
            