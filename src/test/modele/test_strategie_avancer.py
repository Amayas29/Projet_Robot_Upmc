from controller.strategies import Avancer
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
from model.obstacles import Obstacle


def test():

    arene = Arene()
    robot = Robot(Point(100, 100), arene)
    arene.set_robot(robot)

    robot.servo_rotate(90)
    src = Point(300, 100)
    dest = Point(800, 100)

    obstacle = Obstacle(src, dest)
    arene.add_obstacle(obstacle)

    affichage = Affichage(arene)
    controleur = Controleur()
    avancer = Avancer(robot, 175, 100)
    controleur.add_startegie(avancer)
    controleur.select_startegie(0)

    FPS = 60.

    while True:
        controleur.update()
        arene.update()
        affichage.update(FPS)
