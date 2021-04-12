from threading import Thread
from utils.config import Config
from controller.controleur import Controleur
from controller.strategies import Carre, Triangle,  Avancer, Tourner


controleur = Controleur()

# protection du config
config = Config()

if (config.get_vers() != 0.4):
    print("Config version non conforme")
    print(config.get_vers())
    exit(1)

if (config.get_dist_secu() < 13.0):
    print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
    exit(1)

mode = config.get_mode()

FPS = config.get_fps()

if (mode):  # Mode Simu
    print("Simu on")

    from view.affichage import Affichage
    from model.robot import Robot
    from model.arene import Arene
    from utils.tools import Point
    from model.obstacles import Obstacle
    import sys

    arene = Arene()
    
    robot = Robot(Point(230, 300), arene)
    arene.set_robot(robot)

    affichage = Affichage(arene)

    # Exo 2 Q.1)
    strat = Triangle(robot, 100, 200, 5)

    #Exo 2 Q.2)
    #strat = Polygone(robot, 80 ,200,1,8)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()
