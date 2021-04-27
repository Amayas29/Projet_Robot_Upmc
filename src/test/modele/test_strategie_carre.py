from pathlib import Path
import sys
from threading import Thread

root_dir = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(root_dir))

if str(root_dir) in sys.path:

    from controller.wrapper import Wrapper
    from view.affichage import Affichage
    from utils.tools import Point
    from model.arene import Arene
    from model.robot import Robot
    from controller.controleur import Controleur
    from controller.strategies import Carre


arene = Arene()
centre = Point(500, 500)

robot = Robot(centre, arene)
arene.set_robot(robot)

robot.servo_rotate(90)

affichage = Affichage(arene)
controleur = Controleur()

robot = Wrapper(robot)
carre = Carre(robot, 100, 300, 0, 50)

controleur.add_startegie(carre)
controleur.select_startegie(0)

FPS = 60.

thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
thread_modele = Thread(target=arene.boucle, args=(FPS,))
thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

thread_controleur.start()
thread_modele.start()
thread_affichage.start()
