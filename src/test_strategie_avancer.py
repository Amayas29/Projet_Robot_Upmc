from controleur.strategies import Avancer
from controleur.controleur import Controleur
from modele.robot import Robot
from modele.modele import Modele
from modele.arene import Arene
from utils.tools import Point
from view.affichage import Affichage
from modele.obstacles import Obstacle

centre = Point(50, 50)
robot = Robot(centre, 50, 50, 0)


arene = Arene()
arene.set_robot(robot)

src = Point(300 , 50)
dest = Point( 500 , 500 )

obstacle = Obstacle(src, dest)
arene.add_obstacle(obstacle)
modele = Modele(60., arene)

controleur = Controleur(robot, arene, 60.)
avancer = Avancer(robot, 50, 50)
controleur.add_startegie(avancer)
controleur.select_startegie(0)

affichage = Affichage(arene, 60.)


while True:
    # print(robot.chg, robot.cbg, robot.chd, robot.cbd)
    controleur.update()
    modele.update()
    affichage.update()
