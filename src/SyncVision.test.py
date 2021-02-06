from Vision import *
from Tool import *
from Simulation import *
from Robot import *
import random

rob = Robot(5)
rob.setSimu(True)
sim = rob.simu

for i in range (sim.larg):
    for j in range(sim.long):
        if str(sim.grille[i][j]) != "R" and random.randint(0, 5) == 0:
            sim.grille[i][j] = Wall()

add_Objet(sim.grille, Objet(), 2, 5)
add_Objet(sim.grille, Objet(), 8, 1)

affiche(sim.grille)

print(sim.vision.larg)

print("\n\n")
sim.robotSimu.direction = 200

rob.simu.syncVision()