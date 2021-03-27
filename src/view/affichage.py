from time import sleep
import pygame
import sys

pygame.init()
pygame.display.set_caption("Affichage")
p = pygame.display.set_mode( (1090 , 920) )
CLOCK = pygame.time.Clock()

#colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0 ,0 ,255 )
RED = (255 ,0 ,0 )


class Affichage:

    def __init__(self, arene, fps):
        self.fps = fps
        self.arene = arene
        self.robot = arene.robot


    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
      self.events()
      CLOCK.tick( self.fps )
      for (src,dest) in self.arene.elements:
        pygame.draw.line( p , WHITE , src , dest , 50)
    
      pygame.draw.line( p , BLUE , self.robot.chg , self.robot.chd , 10)
      pygame.draw.line( p , BLUE , self.robot.chg , self.robot.cbg , 10)
      pygame.draw.line( p , RED , self.robot.chd , self.robot.cbd , 10)
      pygame.draw.line( p , BLUE , self.robot.cbg , self.robot.cbd , 10)
       
      pygame.display.flip()

  
    def events():
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


