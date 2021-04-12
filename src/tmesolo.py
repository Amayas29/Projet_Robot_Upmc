from controller.strategies import Triangle, PolygoneRegulier
from controller.controleur import Controleur
from threading import Thread
from utils.tools import Point
from model.robot import Robot
from model.arene import Arene
from view.affichage import Affichage

FPS = 60


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


if __name__ == '__main__':
    q2_2()
