from time import sleep
import pygame
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
        self.debug = True

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
        if self.old is None:
            self.old  = Point(self.robot.x, self.robot.y)

        if self.robot.trait==0:
            pygame.draw.line(self.p, BLUE, (self.old.x, self.old.y),
                             (self.robot.center.x, self.robot.center.y), self.epaisseur)

        self.display_debug()

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    def display_debug(self):

        if self.debug:
            a = Point.milieu(self.robot.chd, self.robot.cbd)
            b = Point(
                a.x + self.robot.vec_deplacement.vect[0]*100, a.y + self.robot.vec_deplacement.vect[1]*100)
            pygame.draw.line(self.p, RED, (a.x, a.y),
                             (b.x, b.y), self.epaisseur)
            m1 = Point((self.robot.cbg.x + self.robot.cbd.x)/2,
                       (self.robot.cbg.y + self.robot.cbd.y)/2)
            m2 = Point((self.robot.chg.x + self.robot.chd.x)/2,
                       (self.robot.chg.y + self.robot.chd.y)/2)

            pygame.draw.line(self.p, RED, (m2.x, m2.y),
                             (m1.x, m1.y), self.epaisseur)

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
            if new_milieu == None:
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
