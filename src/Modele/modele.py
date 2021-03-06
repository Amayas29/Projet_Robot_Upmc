from   time import sleep
import threading

class Modele:

    def __init__(self, fps):
        self.fps = fps

    
    def update_modele():
        while True:
            sleep(1./fps)