from controller.strategies import Tourner
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point
from view.affichage import Affichage


def test():
    arene = Arene()
    centre = Point(900, 900)
    robot = Robot(centre, 50, 50, arene)
    arene.set_robot(robot)

    controleur = Controleur()
    tourner = Tourner(robot, 180, 0, 50)
    controleur.add_startegie(tourner)
    controleur.select_startegie(0)

    affichage = Affichage(arene)

    FPS = 60.

    while True:
        # print(robot.chg, robot.cbg, robot.chd, robot.cbd)
        controleur.update()
        arene.update()
        affichage.update(FPS)
