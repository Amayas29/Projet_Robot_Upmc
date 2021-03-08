from threading import Thread
from Gui.affichage import Affichage
from Controleur.controleur import Controleur
from Modele.robot import Robot
from Modele.arene import Arene
from Controleur.vision import Vision

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