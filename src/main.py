from threading import Thread

from controller.controleur import Controleur
from controller.strategies import Carre
from irl.mockup import Robot2I013Mockup
# from robot2I013 import Robot2I013
# from view.affichage import Affichage

# from model.robot import Robot
# from model.arene import Arene
# from model.obstacles import Obstacle
# from utils.tools import Point


# import configparser
# # protection du config
# config = configparser.ConfigParser()

# config.read('config.cfg')
# if (float(config['Version']['config_version']) != 0.2):
#     print("Config version non conforme")
#     exit(1)
# if (float(config['Robot']['distance_securite']) < 13.0):
#     print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
#     exit(1)
# mode = config['Robot'].getboolean('mode_simu')
# if (mode):
#     print("Simu on")
# else:
#     print("simu off")
# programe

# arene = Arene()
# centre = Point(100, 100)
# robot = Robot(centre, 50, 50, arene)

# robot = Robot2I013()
robot = Robot2I013Mockup()

# arene.set_robot(robot)

# src = Point(300, 100)
# dest = Point(800, 100)

# obstacle = Obstacle(src, dest)
# arene.add_obstacle(obstacle)

controleur = Controleur()
carre = Carre(robot, 500, 250, 1)
controleur.add_startegie(carre)
controleur.select_startegie(0)

# affichage = Affichage(arene)

FPS = 60.0

# thread_affichage = Thread(target=affichage.boucle, args=(FPS,))
thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
# thread_modele = Thread(target=arene.boucle, args=(FPS,))

thread_controleur.start()

robot.stop()
# thread_modele.start()
# thread_affichage.start()

# robot.stop()
