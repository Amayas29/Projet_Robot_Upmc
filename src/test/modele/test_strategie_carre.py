from controller.strategies import Carre
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
import time


def test():

    arene = Arene()
    centre = Point(500, 500)
    robot = Robot(centre, arene)
    arene.set_robot(robot)

    robot.servo_rotate(90)

    affichage = Affichage(arene)
    controleur = Controleur()
    carre = Carre(robot, 100, 100, 0)
    controleur.add_startegie(carre)
    controleur.select_startegie(0)

    FPS = 60.

    while True:
        controleur.update()
        arene.update()
        affichage.update(FPS)
