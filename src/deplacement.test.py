from robot import *
from simulation import *
from tool import *

#test la méthode forward qui permet de déplacer le robot

# rob = Robot(8) Pas encore
rob = Robot(4)
rob.set_simu(True)

# rob.simu.forward(50, 0) Pas encore
# rob.simu.forward(2, 20) Pas encore

# il avance de 18 cases
affiche(rob.simu.grille)

rob.simu.forward(2, 20)

affiche(rob.simu.grille)