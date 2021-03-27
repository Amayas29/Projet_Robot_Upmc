from threading import Thread
from view.affichage import Affichage
from controleur.controleur import Controleur
from modele.robot import Robot
from modele.arene import Arene
from modele.vision import Vision
from utils.tools import Point
import configparser
# protection du config
config = configparser.ConfigParser()

config.read('config.cfg')
if (float(config['Version']['config_version']) != 0.2):
    print("Config version non conforme")
    exit(1)
if (float(config['Robot']['distance_securite']) < 13.0):
    print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
    exit(1)
mode = config['Robot'].getboolean('mode_simu')
if (mode):
    print("Simu on")
else:
    print("simu off")
# programe

robot = Robot(Point(10, 10), 3, 3, 3)
arene = Arene()
vision = Vision(5, 3)

affichage = Affichage(60)
controleur = Controleur(vision, robot, arene, 60)

thread_affichage = Thread(target=affichage.boucle)
thread_controleur = Thread(target=controleur.boucle)
thread_modele = Thread(target=arene.boucle)

thread_controleur.start()
thread_modele.start()
thread_affichage.start()
