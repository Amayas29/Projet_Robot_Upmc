import pygame
from rotate import get_rect , rotate
import math

pygame.init()

pygame.display.set_caption("Test") # titre

p = pygame.display.set_mode( (1090 , 920) ) # taille fenetre

running = True

#positions robot
x = 1090 / 2
y = 920 / 2

#couleurs objets
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

# robot
carre = get_rect(50, 100, WHITE, BLACK)
rect = carre.get_rect()  
rect.center = (x, y) 

#Obstacle
# voir pour utiliser les listes et mettre plusieurs obstacles
obs = get_rect(50, 50, (255, 0, 0), BLACK)
o = obs.get_rect()
o.center = (300, 300)

CLOCK = pygame.time.Clock()

# angle de base du robot
total_angle = -90

#methode move
def deplacement(s, x, y, dist, angle):

    global obs, o

    vitesse = 5
    rad = math.radians(angle)
    dist = dist / vitesse
    dx = math.cos(rad) * vitesse
    dy = math.sin(rad) * vitesse

    while dist > 0:
        dist -= 1
        x += dx
        y += dy
        rect = s.get_rect()
        rect.center = (x, y)

        CLOCK.tick( 120 )  
        p.fill(BLACK)  
        p.blit(s, rect)
        p.blit( obs , o )
        pygame.display.update()
        if rect.collidelist([ o ]) != -1:
            print("Obstacle !")
            return x, y


    return x, y

# fait tourner la demo
while running:

  pygame.display.flip()

  CLOCK.tick( 120 )  #pour charger les objets
  p.fill(BLACK)  
  p.blit(carre, rect)
  p.blit(obs, o)
  pygame.display.update() 

  for event in pygame.event.get() :

    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fin de la démonstration")

  a = float(input("Donner l'angle : "))
  d = float(input("Donner la dist : "))
  print()

  old = (x, y)
  carre = rotate(carre, a)
  rect = carre.get_rect()
  rect.center = old

  CLOCK.tick( 120 )  
  p.fill(BLACK)  
  p.blit(carre, rect)
  p.blit(obs, o)
  pygame.display.update() 

  total_angle -= a
  x, y = deplacement(carre, x, y, d, total_angle)
  rect.center = (x, y)
