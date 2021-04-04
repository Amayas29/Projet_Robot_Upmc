from controller.strategies import Avancer, Tourner
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point, Vecteur
from view.affichage import Affichage
from model.obstacles import Obstacle


def test():

    arene = Arene()
    robot = Robot(Point(433, 500), arene)

    robot.vec_deplacement = Vecteur.get_vect_from_angle(30)
    robot.refresh()

    arene.set_robot(robot)

    robot.servo_rotate(90)
    arene.add_obstacle(Obstacle(Point(900, 500), Point(100, 700)))

    affichage = Affichage(arene)
    controleur = Controleur()

    avancer = Avancer(robot, 175, 600)

    controleur.add_startegie(avancer)
    controleur.select_startegie(0)

    FPS = 60.

    while True:

        controleur.update()
        arene.update()
        affichage.update(FPS)
