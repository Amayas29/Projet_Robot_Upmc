from Vision import *
from Tool import *
from Simulation import *
from Robot import *
import random

rob = Robot(5)
rob.setSimu(True)
sim = rob.simu

print("\n\n")

add_Objet(sim.grille, Objet(), 30, 25)
add_Objet(sim.grille, Objet(), 30, 24)
add_Objet(sim.grille, Objet(), 30, 23)
add_Objet(sim.grille, Objet(), 30, 22)
add_Objet(sim.grille, Objet(), 30, 21)
add_Objet(sim.grille, Objet(), 30, 27)
add_Objet(sim.grille, Objet(), 30, 26)
add_Objet(sim.grille, Objet(), 29, 22)
add_Objet(sim.grille, Objet(), 29, 21)
add_Objet(sim.grille, Objet(), 29, 27)
add_Objet(sim.grille, Objet(), 29, 26)
add_Objet(sim.grille, Objet(), 28, 26)
add_Objet(sim.grille, Objet(), 31, 27)
add_Objet(sim.grille, Objet(), 27, 26)

# Attention ! Le robot est encore dans la vision 
# faut encore plus de precision et enlever la ligne du robot
# Pour voir ça : 
# add_Objet(sim.grille, Objet(), 25, 26)

affiche(sim.grille)

print("\n\n")
sim.robotSimu.direction = 0

print("Angle ", sim.robotSimu.direction, "°\n\n")

rob.simu.syncVision()