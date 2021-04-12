from controller.strategies import Triangle, PolygoneRegulier, Avancer, EviterObstacle
from controller.controleur import Controleur
from threading import Thread
from utils.tools import Point, Vecteur
from model.robot import Robot
from model.arene import Arene
from view.affichage import Affichage
from model.obstacles import Obstacle
import random
from time import sleep

FPS = 60


def q1_1():
    """
    Les changements sont fait dans le fichier robot.py et dans affichage.py
    """
    return


def boucle(robot):
    while True:
        if robot.crayon:
            robot.up()
        else:
            robot.down()

        sleep(1)


def q1_2():
    controleur = Controleur()

    arene = Arene()
    robot = Robot(Point(500, 500), arene)
    arene.set_robot(robot)
    strat = Avancer(robot, 400, 300)

    affichage = Affichage(arene)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))
    thread_crayon = Thread(target=boucle, args=(arene.robot))

    thread_controleur.start()
    thread_crayon.start()
    thread_modele.start()
    thread_affichage.start()


def q2_1():

    controleur = Controleur()

    arene = Arene()
    robot = Robot(Point(500, 500), arene)

    arene.set_robot(robot)
    strat = Triangle(robot, 100, 300, 1)

    affichage = Affichage(arene)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()


def q2_2():

    controleur = Controleur()

    arene = Arene()
    robot = Robot(Point(500, 500), arene)
    robot.down()

    arene.set_robot(robot)
    strat = PolygoneRegulier(robot, 8, 100, 300, 1)

    affichage = Affichage(arene)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()


def q2_3():

    controleur = Controleur()

    arene = Arene()
    x = random.randint(100, 900)
    y = random.randint(50, 850)
    robot = Robot(Point(x, y), arene)

    angle = random.randint(0, 360)
    robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)
    robot.refresh()

    arene.add_obstacle(Obstacle(Point(0, 0), Point(1090, 0)))
    arene.add_obstacle(Obstacle(Point(0, 0), Point(0, 920)))
    arene.add_obstacle(Obstacle(Point(1090, 0), Point(1090, 920)))
    arene.add_obstacle(Obstacle(Point(0, 920), Point(1090, 920)))

    arene.set_robot(robot)
    strat = EviterObstacle(robot, 300, float("inf"), float("inf"), 50)

    affichage = Affichage(arene)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()


def q3_1():
    pass


if __name__ == '__main__':
    q2_2()
