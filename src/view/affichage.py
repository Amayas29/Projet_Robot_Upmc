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
        for obs in self.arene.elements:
            src = obs.segment.src
            dest = obs.segment.dest
            pygame.draw.line( p , WHITE , (src.x, src.y) , (dest.x, dest.y) , 10)

        pygame.draw.line( p , BLUE , (self.robot.chg.x, self.robot.chg.y) , (self.robot.chd.x, self.robot.chd.y) , 10)
        pygame.draw.line( p , BLUE , (self.robot.chg.x , self.robot.chg.y) , (self.robot.cbg.x , self.robot.cbg.y) , 10)
        pygame.draw.line( p , RED  , (self.robot.chd.x, self.robot.chd.y) , (self.robot.cbd.x, self.robot.cbd.y), 10)
        pygame.draw.line( p , BLUE , (self.robot.cbg.x , self.robot.cbg.y) , (self.robot.cbd.x , self.robot.cbd.y) , 10)
        
        pygame.display.flip()

  
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


