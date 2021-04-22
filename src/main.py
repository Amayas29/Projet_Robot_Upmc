from threading import Thread
from utils.config import Config
from controller.controleur import Controleur
from controller.strategies import Carre, Triangle, EviterObstacle, Unitaire, Avancer, Tourner, SuivreBalise
from controller.wrapper import Wrapper

controleur = Controleur()

# protection du config
# config = Config()

# if (config.get_vers() != 0.4):
#     print("Config version non conforme")
#     print(config.get_vers())
#     exit(1)

# if (config.get_dist_secu() < 13.0):
#     print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
#     exit(1)

# mode = config.get_mode()

# FPS = config.get_fps()

mode = True
FPS = 60

if (mode):  # Mode Simu
    print("Simu on")

    from view.affichage import Affichage
    from model.robot import Robot
    from model.arene import Arene
    from utils.tools import Point
    from model.obstacles import Obstacle, Balise
    import sys

    arene = Arene()
    balise = Balise(Point(550, 500), Point(500, 550))
    arene.set_balise(balise)

    # obstacles = config.get_obstacles()
    # for obstacle in obstacles:
    #     arene.add_obstacle(obstacle)

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

    #arene.add_obstacle(Obstacle(Point(500, 500), Point(700, 100)))
    # arene.add_obstacle(Obstacle(Point(500, 450), Point(900, 450)))

    affichage = Affichage(arene)

    wrapper = Wrapper(robot)

    # def f(): return wrapper.get_distance() <= 30
    # strat = Unitaire(Avancer(wrapper, 100000, 300), f)

    # strat = Tourner(wrapper, 90, 1, 300 )
    # strat = Carre(wrapper, 100, 300, 1 , 50)
    # strat = Triangle(wrapper, 100, 300, 1 , 50)

    # strat = EviterObstacle(wrapper, 300, 1000, 90, 50)
    strat = SuivreBalise(wrapper, 300)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()

else:  # mode REEL
    print("simu off")

    try:
        from robot2I013 import Robot2I013
        robot = Robot2I013()
    except ImportError:
        from irl.mockup import Robot2I013Mockup
        robot = Robot2I013Mockup()

    strat = Carre(robot, 50, 300, 0)
    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))

    thread_controleur.start()
