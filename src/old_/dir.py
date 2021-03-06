import math, sys
import pygame
from rotate import get_rect, rotate

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def move(s, x, y, dist, ang):

    global wall, rec_wall

    vt = 5
    rad = math.radians(ang)
    dist = dist / vt
    dx = math.cos(rad) * vt
    dy = math.sin(rad) * vt

    while dist > 0:
        dist -= 1
        x += dx
        y += dy
        rect = s.get_rect()
        rect.center = (x, y)

        CLOCK.tick(FPS)  
        DS.fill(BLACK)  
        DS.blit(s, rect)
        DS.blit(wall, rec_wall)
        pygame.display.update()
        if rect.collidelist([rec_wall]) != -1:
            print("OK")
            return x, y


    return x, y


W, H = 1090, 920
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Direction and dist")
FPS = 120

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

x, y = W / 2, H / 2
surf = get_rect(50, 100, WHITE, BLACK)
rect = surf.get_rect()  
rect.center = (x, y) 

wall = get_rect(50, 50, (255, 0, 0), BLACK)
rec_wall = wall.get_rect()
rec_wall.center = (300, 300)

total_angle = 90

while True:
    events()

    CLOCK.tick(FPS)  
    DS.fill(BLACK)  
    DS.blit(surf, rect)
    DS.blit(wall, rec_wall)
    pygame.display.update() 
    
    a = float(input("Donner l'angle : "))
    d = float(input("Donner la dist : "))
    print()

    old = (x, y)
    surf = rotate(surf, a)
    rect = surf.get_rect()
    rect.center = old

    CLOCK.tick(FPS)  
    DS.fill(BLACK)  
    DS.blit(surf, rect)
    DS.blit(wall, rec_wall)
    pygame.display.update() 

    total_angle -= a
    x, y = move(surf, x, y, d, total_angle)
    rect.center = (x, y)