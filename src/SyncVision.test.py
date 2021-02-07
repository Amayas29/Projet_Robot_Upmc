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

affiche(sim.grille)

print("\n\n")
sim.robotSimu.direction = 00

print("Angle ", sim.robotSimu.direction, "°\n\n")

rob.simu.syncVision()