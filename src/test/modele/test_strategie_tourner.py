from controller.strategies import Tourner
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
import time


def test():
    arene = Arene()
    centre = Point(100, 100)
    robot = Robot(centre, arene)
    arene.set_robot(robot)

    controleur = Controleur()
    tourner = Tourner(robot, 90, 0, 100)
    controleur.add_startegie(tourner)
    controleur.select_startegie(0)

    affichage = Affichage(arene)

    FPS = 60.

    while True:
        controleur.update()
        arene.update()
        affichage.update(FPS)

        # Ce bg pose un probleme ! (Hamid c'etait pas moi le probleme xD !)
        time.sleep(1)
