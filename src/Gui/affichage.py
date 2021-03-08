from time import sleep
import pygame as py
import sys

class Affichage:

    def __init__(self, arene, fps):
        self.fps = fps
        self.arene = arene


    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
        # Pygames ?
        pass

    def events():
      for event in py.event.get():
        if event.type == py.QUIT:
          py.quit()
          sys.exit()

  