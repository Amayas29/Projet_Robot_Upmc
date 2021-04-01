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
        
        affichage.update(FPS)
        controleur.update()
        arene.update()
        time.sleep(1)
        
