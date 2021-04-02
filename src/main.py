from threading import Thread
from utils.tools import Config
# protection du config
config = Config()
if ( config.get_vers() != 0.2):
  print("Config version non conforme")
  print(config.get_vers())
  exit(1)

if ( config.get_dist_secu() < 13.0):
  print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
  exit(1)

mode = config.get_mode()
if (mode):
  print("Simu on")
else:
  print("simu off")
# programe

FPS = 60.0

if (mode):  #Mode Simu
  from view.affichage import Affichage
  from model.robot import Robot
  from model.arene import Arene
  from utils.tools import Point
  arene = Arene()
  centre = Point(100, 100)
  robot = Robot(centre, arene)
  arene.set_robot(robot)
  affichage = Affichage(arene)
  thread_affichage = Thread(target=affichage.boucle, args=(FPS,))
  thread_modele = Thread(target=arene.boucle, args=(FPS,))
  thread_modele.start()
  thread_affichage.start()
else:  #mode REEL
  from controller.controleur import Controleur
  from controller.strategies import Carre
# from irl.mockup import Robot2I013Mockup
  from robot2I013 import Robot2I013
  controleur = Controleur()
  robot = Robot2I013(controleur)
  carre = Carre(robot, 50, 300, 0)
  controleur.add_startegie(carre)
  controleur.select_startegie(0)
  thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
  thread_controleur.start()





