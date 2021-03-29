from controleur.strategies import Tourner
from controleur.controleur import Controleur
from modele.robot import Robot
from modele.arene import Arene
from utils.tools import Point
from view.affichage import Affichage

def test():
    centre = Point(100, 800)
    robot = Robot(centre, 50, 50)

    arene = Arene()
    arene.set_robot(robot)

    controleur = Controleur(arene)
    tourner = Tourner(robot, 90, 0)
    controleur.add_startegie(tourner)
    controleur.select_startegie(0)

    affichage = Affichage(arene)

    FPS = 60.

    i = 0
    while True:
        # print(robot.chg, robot.cbg, robot.chd, robot.cbd)
        controleur.update()
        if i <= 90:
            arene.update()
            i += 0.5
        affichage.update(FPS)
