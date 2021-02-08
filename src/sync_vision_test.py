from vision import *
from tool import *
from simulation import *
from robot import *
import random

rob = Robot(8)
rob.set_simu(True)
sim = Simulation(5, 5,rob.echelle, rob.vision, rob.taille_robot)
rob.simu = sim
random.seed(30)
for i in range(len(sim.grille)):
   for j in range(len(sim.grille[0])):
       if str(sim.grille[i][j]) != "RR":
          sim.grille[i][j] = random.choice("ABCDEFGHIJKLMNOPQSTUVXYZ")

# sim.grille[20][20] = '1'

# x = random.randint(0, 39)
# y = random.randint(0, 39)

# print( "\n\nPosition robot :\nx = " + str(x) + " , y = " + str(y) )

# sim.grille[x][y] = rob.simu.robot_simu
# rob.simu.robot_simu.set_pos(x, y, 0)

print("\n\n")

# add_objet_(sim.grille, Objet(), 30, 25)
# add_objet_(sim.grille, Objet(), 30, 24)
# add_objet_(sim.grille, Objet(), 30, 23)
# add_objet_(sim.grille, Objet(), 30, 22)
# add_objet_(sim.grille, Objet(), 30, 21)
# add_objet_(sim.grille, Objet(), 30, 27)
# add_objet_(sim.grille, Objet(), 30, 26)
# add_objet_(sim.grille, Objet(), 29, 22)
# add_objet_(sim.grille, Objet(), 29, 21)
# add_objet_(sim.grille, Objet(), 29, 27)
# add_objet_(sim.grille, Objet(), 29, 26)
# add_objet_(sim.grille, Objet(), 28, 26)
# add_objet_(sim.grille, Objet(), 31, 27)
# add_objet_(sim.grille, Objet(), 27, 26)

add_objet_(sim.grille,'A', 21, 20)
add_objet_(sim.grille, 'B', 21, 21)
add_objet_(sim.grille,'C', 21, 22)
add_objet_(sim.grille, 'D', 21, 19)
add_objet_(sim.grille, 'E', 21, 18)
add_objet_(sim.grille, "F", 21, 22)
add_objet_(sim.grille,'G', 21, 17)
add_objet_(sim.grille, 'H', 21, 16)
add_objet_(sim.grille,'I', 21, 23)
add_objet_(sim.grille, 'K', 21, 24)
add_objet_(sim.grille, 'L', 21, 15)
add_objet_(sim.grille, "M", 21, 25)
add_objet_(sim.grille,'N', 21, 14)
add_objet_(sim.grille, 'O', 21, 13)
add_objet_(sim.grille, 'P', 21, 26)
add_objet_(sim.grille, "Q", 21, 27)
add_objet_(sim.grille, "T", 21, 28)
add_objet_(sim.grille, "S", 21, 12)

add_objet_(sim.grille,'$', 36, 20)

add_objet_(sim.grille,'£', 30, 20)

add_objet_(sim.grille,'7', 20, 21)
add_objet_(sim.grille,'1', 19, 21)

affiche(sim.grille)

print("\n\n")

sim.robot_simu.direction = normalise_angle(int(input("Direction : ")))

src = get_src_point(sim.taille_robot, sim.robot_simu.posx, sim.robot_simu.posy, sim.robot_simu.direction)

print(src)

print("Angle ", sim.robot_simu.direction, "°\n\n")

rob.simu.sync_vision()