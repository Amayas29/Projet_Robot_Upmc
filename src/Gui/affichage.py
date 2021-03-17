from time import sleep
import pygame 
import sys

pygame.init()
pygame.display.set_caption("Affichage")
p = pygame.display.set_mode( (1090 , 920) )

class Affichage:

    def __init__(self, arene, fps):
        self.fps = fps
        self.arene = arene


    def boucle(self):
        while True:
            self.update()
            sleep(1./self.fps)


    def update(self):
      #CLOCK.tick( fps )
      #for e in elements : 
        #xx = e.
        #obs = get_rect( xx, yy , (250 ,0 ,0), BLACK)
       # o = obs.get_rect()
        #o.center = ( xx , yy )
        #p.blit(obs, o)
      #pygame.display.update()
      pass
     
        






    def events():
      for event in py.event.get():
        if event.type == py.QUIT:
          py.quit()
          sys.exit()


BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
run = True

elements = [ (0,200,100,200) , (100,100,100,200) , (0,100,100,100)  ]




while run :
  for event in pygame.event.get() :

    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fin de la démonstration")

  for (x1,x2,y1,y2) in elements:
    pygame.draw.line( p , WHITE , (x1,x2) , (y1,y2) , 10)
  pygame.display.flip()


