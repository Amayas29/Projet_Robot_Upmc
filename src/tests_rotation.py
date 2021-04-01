from time import sleep
import pygame
import sys
from utils.tools import Point, Vecteur, Droite

# colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
AUTRE = (235, 152, 135)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



p1 = Point(400,400)
p2 = Point(300,200)
p3 = Point(600,100)
p4 = Point(700,300)
m1 = Point((p1.x + p4.x)/2,(p1.y + p4.y)/2)
m2 = Point((p3.x + p2.x)/2,(p3.y + p2.y)/2)
angle = 0
while True:
    pygame.init()
    pygame.display.set_caption("Affichage")
    p = pygame.display.set_mode((1090, 920))
    CLOCK = pygame.time.Clock()
    epaisseur = 5

    p.fill(BLACK)
    events()
    CLOCK.tick(60)

    pygame.draw.line(p, BLUE, (p1.x, p1.y),(p2.x, p2.y), epaisseur)
    pygame.draw.line(p, BLUE, (p2.x, p2.y),(p3.x, p3.y), epaisseur)
    pygame.draw.line(p, BLUE, (p3.x, p3.y),(p4.x, p4.y), epaisseur)
    pygame.draw.line(p, BLUE, (p4.x, p4.y),(p1.x, p1.y), epaisseur)

    
    pygame.draw.line(p, RED, (m2.x, m2.y),(m1.x, m1.y), epaisseur)
    m1 = Point((p1.x + p4.x)/2,(p1.y + p4.y)/2)
    m2 = Point((p3.x + p2.x)/2,(p3.y + p2.y)/2)


    print(m1)
    p1.rotate(m1,angle)
    p2.rotate(m1,angle)
    p3.rotate(m1,angle)
    p4.rotate(m1,angle)
    angle+= 1
    sleep(1)


    pygame.display.flip()