from controller.strategies import Avancer, Tourner
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
from model.obstacles import Obstacle


def test():

    arene = Arene()
    robot = Robot(Point(433, 300), arene)
    robot.vec_deplacement.vect = (1.0, -0.07)
    robot.refresh()
    arene.set_robot(robot)

    robot.servo_rotate(90)
    arene.add_obstacle(Obstacle(Point(300, 260), Point(900, 255)))

    affichage = Affichage(arene)
    controleur = Controleur()
    avancer = Avancer(robot, 175, 300)
    tourner = Tourner(robot, 90, 1, 300)
    controleur.add_startegie(avancer)

    controleur.add_startegie(tourner)
    controleur.select_startegie(0)

    FPS = 60.

    cpt = 0
    while True:
        if avancer.is_stop:
            cpt += 1

            # if cpt < 3:
            controleur.select_startegie(1)
            # else:
            #     robot.servo_rotate(60)

        if tourner.is_stop:
            # cpt += 1
            # if cpt < 3:

                robot.servo_rotate(90)
                avancer.start()
                controleur.select_startegie(0)

        controleur.update()
        arene.update()
        affichage.update(FPS)
