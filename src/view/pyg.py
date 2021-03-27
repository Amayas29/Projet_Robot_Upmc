from time import sleep
import pygame
import sys

pygame.init()
pygame.display.set_caption("Affichage")
p = pygame.display.set_mode((1090, 920))

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

elements = [(0, 200, 100, 200), (100, 100, 100, 200),
            (0, 100, 100, 100), (500, 20, 20, 500)]

chg = (300, 300)
chd = (320, 300)
cbg = (300, 330)
cbd = (320, 330)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fin de la démonstration")
            sys.exit()

    for (x1, x2, y1, y2) in elements:
        pygame.draw.line(p, WHITE, (x1, x2), (y1, y2), 10)

    pygame.draw.line(p, BLUE, chg, chd, 10)
    pygame.draw.line(p, BLUE, chg, cbg, 10)
    pygame.draw.line(p, RED, chd, cbd, 10)
    pygame.draw.line(p, BLUE, cbg, cbd, 10)

    pygame.display.flip()
