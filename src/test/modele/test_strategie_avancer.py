from controleur.strategies import Avancer
from controleur.controleur import Controleur
from modele.robot import Robot
from modele.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
from modele.obstacles import Obstacle
from time import sleep


def test():
    centre = Point(100, 100)
    robot = Robot(centre, 50, 50)

    arene = Arene()
    arene.set_robot(robot)

    src = Point(300, 0)
    dest = Point(300, 800)

    obstacle = Obstacle(src, dest)
    arene.add_obstacle(obstacle)

    controleur = Controleur(arene)
    avancer = Avancer(robot, 50, 50)
    controleur.add_startegie(avancer)
    controleur.select_startegie(0)

    affichage = Affichage(arene)

    FPS = 60.

    while True or not arene.robot.vision.check_collisions():
        # print(robot.chg, robot.cbg, robot.chd, robot.cbd)
        controleur.update()
        arene.update()
        # print(arene.robot.vision.elements)
        affichage.update(FPS)


# if __name__ == "__main__":
#    a = '/home/runner/ProjetRobotUpmc/src'
#    sys.path.insert(0, a)
#    "cd ../.. ; pwd"
#    sys.insert(0, )
#    test()
