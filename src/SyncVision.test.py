from Vision import *
from Tool import *
from Simulation import *
from Robot import *
import random

rob = Robot(8)
rob.setSimu(True)
sim = rob.simu

for i in range(len(sim.grille)):
   for j in range(len(sim.grille[0])):
       if str(sim.grille[i][j]) != "RR":
          sim.grille[i][j] = random.choice("ABCDEFGHIJKLMNOPQSTUVXYZ")

# sim.grille[20][20] = '1'

# x = random.randint(0, 39)
# y = random.randint(0, 39)

# print( "\n\nPosition robot :\nx = " + str(x) + " , y = " + str(y) )

# sim.grille[x][y] = rob.simu.robotSimu
# rob.simu.robotSimu.setPos(x, y, 0)

print("\n\n")

# add_Objet(sim.grille, Objet(), 30, 25)
# add_Objet(sim.grille, Objet(), 30, 24)
# add_Objet(sim.grille, Objet(), 30, 23)
# add_Objet(sim.grille, Objet(), 30, 22)
# add_Objet(sim.grille, Objet(), 30, 21)
# add_Objet(sim.grille, Objet(), 30, 27)
# add_Objet(sim.grille, Objet(), 30, 26)
# add_Objet(sim.grille, Objet(), 29, 22)
# add_Objet(sim.grille, Objet(), 29, 21)
# add_Objet(sim.grille, Objet(), 29, 27)
# add_Objet(sim.grille, Objet(), 29, 26)
# add_Objet(sim.grille, Objet(), 28, 26)
# add_Objet(sim.grille, Objet(), 31, 27)
# add_Objet(sim.grille, Objet(), 27, 26)

add_Objet(sim.grille,'A', 21, 20)
add_Objet(sim.grille, 'B', 21, 21)
add_Objet(sim.grille,'C', 21, 22)
add_Objet(sim.grille, 'D', 21, 19)
add_Objet(sim.grille, 'E', 21, 18)
add_Objet(sim.grille, "F", 21, 22)
add_Objet(sim.grille,'G', 21, 17)
add_Objet(sim.grille, 'H', 21, 16)
add_Objet(sim.grille,'I', 21, 23)
add_Objet(sim.grille, 'K', 21, 24)
add_Objet(sim.grille, 'L', 21, 15)
add_Objet(sim.grille, "M", 21, 25)
add_Objet(sim.grille,'N', 21, 14)
add_Objet(sim.grille, 'O', 21, 13)
add_Objet(sim.grille, 'P', 21, 26)
add_Objet(sim.grille, "Q", 21, 27)
add_Objet(sim.grille, "T", 21, 28)
add_Objet(sim.grille, "S", 21, 12)

add_Objet(sim.grille,'$', 36, 20)

add_Objet(sim.grille,'£', 30, 20)

affiche(sim.grille)

print("\n\n")

sim.robotSimu.direction = normalise_angle(int(input("Direction : ")))

src = getSrcPoint(sim.taille_robot, sim.robotSimu.posx, sim.robotSimu.posy, sim.robotSimu.direction)

print(src)

print("Angle ", sim.robotSimu.direction, "°\n\n")

rob.simu.syncVision()