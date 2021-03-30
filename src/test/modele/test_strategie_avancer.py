from controller.strategies import Avancer
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point, Vecteur
from view.affichage import Affichage
from model.obstacles import Obstacle


def test():

    arene = Arene()
    centre = Point(100, 100)
    robot = Robot(centre, 50, 50, arene)
    arene.set_robot(robot)

    robot.vec_servo = Vecteur.get_vect_from_angle(30)
    src = Point(300, 100)
    dest = Point(800, 100)

    obstacle = Obstacle(src, dest)
    arene.add_obstacle(obstacle)

    # y = 127
    # src = Point(150, y)
    # dest = Point(200, y)

    # obstacle = Obstacle(src, dest)
    # arene.add_obstacle(obstacle)

    controleur = Controleur()
    avancer = Avancer(robot, 10000000000, 200)
    controleur.add_startegie(avancer)
    controleur.select_startegie(0)

    affichage = Affichage(arene)

    FPS = 60.

    while True:
        # print(robot.vision)
        # print(robot)
        controleur.update()
        arene.update()
        affichage.update(FPS)


# if __name__ == "__main__":
#    a = '/home/runner/ProjetRobotUpmc/src'
#    sys.path.insert(0, a)
#    "cd ../.. ; pwd"
#    sys.insert(0, )
#    test()
