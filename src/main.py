from threading import Thread
from controller.strategies import Tourner
from utils.config import Config
import sys

# protection du config
config = Config()

if (config.get_vers() != 0.3):
    print("Config version non conforme")
    print(config.get_vers())
    exit(1)

if (config.get_dist_secu() < 130.0):
    print("Erreur critique: la distance de sécurité est trop faible! (minimum 130.0)")
    exit(1)

mode = config.get_mode()
if (mode):
    print("Simu on")
else:
    print("simu off")

FPS = 60.0

if (mode):  # Mode Simu
    from view.affichage import Affichage
    from model.robot import Robot
    from model.arene import Arene
    from utils.tools import Point
    from model.obstacles import Obstacle
    from controller.controleur import Controleur
    from controller.strategies import Carre

    arene = Arene()
    controleur = Controleur()

    obstacles = config.get_obstacles()
    for obstacle in obstacles:
        arene.add_obstacle(obstacle)

    # try:
    #     test = int(sys.argv[1])
    # except:
    #     test = 1

    # if test == 1:
    #     arene.add_obstacle(Obstacle(Point(100, 10), Point(900, 900)))
    # elif test == 2:
    #     arene.add_obstacle(Obstacle(Point(100, 270), Point(900, 10)))
    # elif test == 3:
    #     arene.add_obstacle(Obstacle(Point(250, 270), Point(900, 10)))
    # elif test == 4:
    #     arene.add_obstacle(Obstacle(Point(300, 260), Point(900, 260)))
    # else:
    #     arene.add_obstacle(Obstacle(Point(300, 300), Point(900, 300)))

    robot = Robot(Point(230, 300), arene)
    arene.set_robot(robot)

    affichage = Affichage(arene)

    carre = Tourner(robot, 90, 1, 300)
    carre = Carre(robot, 100, 300, 1)
    controleur.add_startegie(carre)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()

else:  # mode REEL
    from controller.controleur import Controleur
    from controller.strategies import Carre

    controleur = Controleur()

    try:
        from robot2I013 import Robot2I013
        robot = Robot2I013(controleur)
    except ImportError:
        from irl.mockup import Robot2I013Mockup
        robot = Robot2I013Mockup()

    carre = Carre(robot, 50, 300, 0)
    controleur.add_startegie(carre)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))

    thread_controleur.start()

print("fin du main")
