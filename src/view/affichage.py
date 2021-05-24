from time import sleep
import pygame
from utils.tools import Point, Vecteur, Droite
from model.obstacles import Balise
from pathlib import Path

from copy import deepcopy

# colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
AUTRE = (235, 152, 135)
YELLOW = (255, 255, 0)


class PygameBalise(pygame.sprite.Sprite):

    """
        Cette classe represente la balise en mode simu, c'est un objet pygame qu'on peut deplacer à l'aide du clavier pour simuler le mouvement de la balise
    """

    def __init__(self, arene):
        super().__init__()
        root_dir = Path(__file__).parent.parent
        self.image = pygame.image.load('{}/balise_simu.png'.format(root_dir))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.velocity = 5
        self.arene = arene
        mil = Point.milieu(arene.balise.segment.src, arene.balise.segment.dest)
        self.rect.x = mil.x
        self.rect.y = mil.y

    def move_right(self):
        """
        None -> None

        Deplacer la balise à droite
        """
        self.rect.x += self.velocity
        self.arene.balise.segment.src.x += self.velocity
        self.arene.balise.segment.dest.x += self.velocity

    def move_left(self):
        """
        None -> None

        Deplacer la balise à gauche
        """
        self.rect.x -= self.velocity
        self.arene.balise.segment.src.x -= self.velocity
        self.arene.balise.segment.dest.x -= self.velocity

    def move_down(self):
        """
        None -> None

        Deplacer la balise en bas
        """
        self.rect.y += self.velocity
        self.arene.balise.segment.src.y += self.velocity
        self.arene.balise.segment.dest.y += self.velocity

    def move_up(self):
        """
        None -> None

        Deplacer la balise en haut
        """
        self.rect.y -= self.velocity
        self.arene.balise.segment.src.y -= self.velocity
        self.arene.balise.segment.dest.y -= self.velocity


class Affichage:

    """
        La classe qui permet d'afficher la simulation en 2D avec pygame
    """

    def __init__(self, arene):
        self.arene = arene
        pygame.init()
        pygame.display.set_caption("Affichage")
        self.p = pygame.display.set_mode((1090, 920))
        self.CLOCK = pygame.time.Clock()
        self.epaisseur = 5
        self.debug = False
        self.balise = PygameBalise(arene)
        self.pressed = {}
        self.old_position = []
        self.run = True

    def boucle(self, fps):
        """
        float -> None

        Boucle qui permet d'actualise l'affichage à chaque pas de temps
        """
        while self.run:
            self.update(fps)
            sleep(1./fps)

    def update(self, fps):
        """
        float -> None

        Permet de reafficher et de redessiner le robot et les obstacles dans la frame
        """

        # On mets le fond en noir
        self.p.fill(BLACK)

        # On dessine la balise
        self.p.blit(self.balise.image, self.balise.rect)

        # On traite les mouvement de la balise (les touches de clavier pour la déplacer)
        if self.pressed.get(pygame.K_RIGHT):
            self.balise.move_right()

        elif self.pressed.get(pygame.K_LEFT):
            self.balise.move_left()

        elif self.pressed.get(pygame.K_UP):
            self.balise.move_up()

        elif self.pressed.get(pygame.K_DOWN):
            self.balise.move_down()

        self.events()
        self.CLOCK.tick(fps)

        # On boucle sur les obstacle et on les dessine
        for obs in self.arene.elements:
            src = obs.segment.src
            dest = obs.segment.dest
            color = WHITE

            if isinstance(obs, Balise):
                color = YELLOW

            pygame.draw.line(self.p, color, (src.x, src.y),
                             (dest.x, dest.y), self.epaisseur)

        # On dessine le robot
        pygame.draw.line(self.p, BLUE, (self.arene.robot.chg.x, self.arene.robot.chg.y),
                         (self.arene.robot.chd.x, self.arene.robot.chd.y), self.epaisseur)
        pygame.draw.line(self.p, BLUE, (self.arene.robot.chg.x, self.arene.robot.chg.y),
                         (self.arene.robot.cbg.x, self.arene.robot.cbg.y), self.epaisseur)
        pygame.draw.line(self.p, RED, (self.arene.robot.chd.x, self.arene.robot.chd.y),
                         (self.arene.robot.cbd.x, self.arene.robot.cbd.y), self.epaisseur)
        pygame.draw.line(self.p, BLUE, (self.arene.robot.cbg.x, self.arene.robot.cbg.y),
                         (self.arene.robot.cbd.x, self.arene.robot.cbd.y), self.epaisseur)

        m1 = Point((self.arene.robot.cbg.x + self.arene.robot.cbd.x)/2,
                   (self.arene.robot.cbg.y + self.arene.robot.cbd.y)/2)
        m2 = Point((self.arene.robot.chg.x + self.arene.robot.chd.x)/2,
                   (self.arene.robot.chg.y + self.arene.robot.chd.y)/2)

        pygame.draw.line(self.p, self.arene.robot.led_color, (m2.x, m2.y),
                         (m1.x, m1.y), self.epaisseur)

        # Si on a pas de points déja sauvegarder on ajoute le centre du robot
        if self.old_position == []:
            self.old_position.append(deepcopy(self.arene.robot.center))

        # Si on a le crayon du robot est baissé pour écrire
        if self.arene.robot.crayon:

            # On parcours les points sauvegardees
            for i in range(1, len(self.old_position)):

                # On reccupere les extremites d'un segment (un segment entre 2 points sauvegardes)
                old_i = self.old_position[i]
                old_i_1 = self.old_position[i-1]

                # Si l'un deux est null on affiche pas c'est un trait discontinue
                if old_i is None or old_i_1 is None:
                    continue

                # Sinon on dessine le segment
                pygame.draw.line(self.p, AUTRE, (old_i_1.x, old_i_1.y),
                                 (old_i.x, old_i.y), self.epaisseur)

            # Et on ajoute le centre du robot
            self.old_position.append(deepcopy(self.arene.robot.center))
        else:
            # Sinon si le crayon est levé on ajoute None
            self.old_position.append(None)

        self.display_debug()

        pygame.display.flip()

    def events(self):
        """
        None -> None

        On reccupere les evenements et les touches clavier
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

    def display_debug(self):
        """
        None -> None

        On affiche les vecteurs et points pour debug  : 

        On affiche les vecteur deplacement, le vecteur servo du robot

        et les droite utilisé dans sync_vision
        """

        if self.debug:

            a = Point.milieu(
                self.arene.robot.chd, self.arene.robot.cbd)

            b = Point(
                a.x + self.arene.robot.vec_deplacement.vect[0]*100, a.y + self.arene.robot.vec_deplacement.vect[1]*100)

            pygame.draw.line(self.p, RED, (a.x, a.y),
                             (b.x, b.y), self.epaisseur)

            largeur = self.arene.robot.chd - self.arene.robot.cbd

            vec_norme = Vecteur(self.arene.robot.chd, self.arene.robot.cbd)
            vec_src = self.arene.robot.vec_servo

            angle = vec_src.angle(vec_norme)
            milieu = self.arene.robot.cbd

            if angle == 90:
                milieu = Point.milieu(
                    self.arene.robot.chd, self.arene.robot.cbd)
            elif angle > 90:
                milieu = self.arene.robot.chd

            a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

            point_servo = Point.milieu(
                self.arene.robot.chd, self.arene.robot.cbd)

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

    def stop(self):
        """
        None -> None

        Permet d'arreter la boucle de l'affichage
        """
        self.run = False
        pygame.quit()
