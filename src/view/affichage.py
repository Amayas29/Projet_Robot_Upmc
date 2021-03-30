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


class Affichage:

    def __init__(self, arene):
        self.arene = arene
        self.robot = arene.robot
        pygame.init()
        pygame.display.set_caption("Affichage")
        self.p = pygame.display.set_mode((1090, 920))
        self.CLOCK = pygame.time.Clock()
        self.epaisseur = 5
        self.debug = False

    def boucle(self, fps):
        while True:
            self.update(fps)
            sleep(1./fps)

    def update(self, fps):
        self.p.fill(BLACK)
        self.events()
        self.CLOCK.tick(fps)
        for obs in self.arene.elements:
            src = obs.segment.src
            dest = obs.segment.dest
            pygame.draw.line(self.p, WHITE, (src.x, src.y),
                             (dest.x, dest.y), self.epaisseur)

        pygame.draw.line(self.p, BLUE, (self.robot.chg.x, self.robot.chg.y),
                         (self.robot.chd.x, self.robot.chd.y), self.epaisseur)
        pygame.draw.line(self.p, BLUE, (self.robot.chg.x, self.robot.chg.y),
                         (self.robot.cbg.x, self.robot.cbg.y), self.epaisseur)
        pygame.draw.line(self.p, RED, (self.robot.chd.x, self.robot.chd.y),
                         (self.robot.cbd.x, self.robot.cbd.y), self.epaisseur)
        pygame.draw.line(self.p, BLUE, (self.robot.cbg.x, self.robot.cbg.y),
                         (self.robot.cbd.x, self.robot.cbd.y), self.epaisseur)

        if self.debug:
            largeur = self.robot.chd - self.robot.cbd

            vec_norme = Vecteur(self.robot.chd, self.robot.cbd)
            vec_src = self.robot.vec_servo

            angle = vec_src.angle(vec_norme)
            milieu = self.robot.cbd

            if angle == 90:
                milieu = Point.milieu(self.robot.chd, self.robot.cbd)
            elif angle > 90:
                milieu = self.robot.chd

            a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

            point_servo = Point.milieu(self.robot.chd, self.robot.cbd)

            new_milieu = Droite.intersection(
                vec_src, point_servo, Vecteur(a, b), a)
            if not new_milieu:
                pass
            else:
                a, b = Point.get_points_distance(
                    new_milieu, vec_src, largeur//2)

            src_ = Point(
                point_servo.x + vec_src.vect[0] * 100, point_servo.y + vec_src.vect[1] * 100)

            pygame.draw.line(self.p, GREEN, (a.x, a.y),
                             (b.x, b.y), self.epaisseur)

            pygame.draw.line(self.p, AUTRE, (src_.x, src_.y),
                             (point_servo.x, point_servo.y), self.epaisseur)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
