from pathlib import Path
import sys
from threading import Thread

root_dir = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(root_dir))

if str(root_dir) in sys.path:

    from controller.wrapper import Wrapper
    from model.obstacles import Obstacle
    from view.affichage import Affichage
    from utils.tools import Point, Vecteur
    from model.arene import Arene
    from model.robot import Robot
    from controller.controleur import Controleur
    from controller.strategies import Avancer


arene = Arene()
robot = Robot(Point(433, 500), arene)

robot.vec_deplacement = Vecteur.get_vect_from_angle(30)
robot.refresh()

arene.set_robot(robot)

robot.servo_rotate(90)
arene.add_obstacle(Obstacle(Point(900, 500), Point(100, 700)))

affichage = Affichage(arene)
controleur = Controleur()

robot = Wrapper(robot)
avancer = Avancer(robot, 175, 600)

controleur.add_startegie(avancer)
controleur.select_startegie(0)

FPS = 60.

thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
thread_modele = Thread(target=arene.boucle, args=(FPS,))
thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

thread_controleur.start()
thread_modele.start()
thread_affichage.start()
