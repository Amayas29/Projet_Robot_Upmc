from controller.strategies import Avancer
from controller.controleur import Controleur
from model.robot import Robot
from model.arene import Arene
from utils.tools import Point, Vecteur
from view.affichage import Affichage
from model.obstacles import Obstacle


def test():

    # y = 127
    # src = Point(150, y)
    # dest = Point(200, y)

    # obstacle = Obstacle(src, dest)
    # arene.add_obstacle(obstacle)



    for i in range (0, 180):
        arene = Arene()
        centre = Point(100, 100)
        robot = Robot(centre, 50, 50, arene)
        arene.set_robot(robot)

        robot.servo_rotate(90)
        src = Point(300, 100)
        dest = Point(800, 100)

        obstacle = Obstacle(src, dest)
        arene.add_obstacle(obstacle)

        affichage = Affichage(arene)
        controleur = Controleur()
        avancer = Avancer(robot, float("inf"), 100)
        controleur.add_startegie(avancer)
        controleur.select_startegie(0)

        FPS = 60.
        try:
            while True:
                # print(robot.vision)
                controleur.update()
                arene.update()
                affichage.update(FPS)
        except KeyboardInterrupt:
            continue


# if __name__ == "__main__":
#    a = '/home/runner/ProjetRobotUpmc/src'
#    sys.path.insert(0, a)
#    "cd ../.. ; pwd"
#    sys.insert(0, )
#    test()
