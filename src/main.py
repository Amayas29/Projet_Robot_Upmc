from threading import Thread
from Gui.affichage import Affichage
from Controleur.controleur import Controleur
from Modele.robot import Robot
from Modele.arene import Arene
from Modele.vision import Vision
from Utils.tools import Point
from Modele.modele import Modele
import configparser
#protection du config
config = configparser.ConfigParser()

config.read('config.cfg')
if (float(config['Version']['config_version']) != 0.2):
  print("Config version non conforme")
  exit()
if (float(config['Robot']['distance_securite']) < 13.0):
  print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
  exit()
mode = config['Robot'].getboolean('mode_simu')
if (mode):
  print("Simu on")
else:
  print("simu off")
#programe

robot = Robot(Point(10, 10), 3, 3, 3)
arene = Arene()
vision = Vision(5, 3)

affichage = Affichage(60)
modele = Modele(60)
controleur = Controleur(vision, robot, arene, 60)

thread_affichage = Thread(target=affichage.boucle)
thread_controleur = Thread(target=controleur.boucle)
thread_modele = Thread(target=modele.boucle)

thread_controleur.start()
thread_modele.start()
thread_affichage.start()