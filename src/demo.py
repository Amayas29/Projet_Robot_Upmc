from robot import Robot
from tool import affiche, normalise_angle, add_objet
from objet import Objet
from wall import Wall
from random import randint, choice, seed
from robotsimu import RobotSimu
from time import sleep

#  DEMO POUR LE CLIENT 10/02/2021

rob = Robot(16)
rob.set_simu(True)
seed(70)

#montre la simulation initiale

print("\n - Etat initial : \n")

affiche(rob.simu.grille)

print("\n - Les coordonnes du robot : (", rob.simu.robot_simu.posy, rob.simu.robot_simu.posx, ")")

print("\n\n - Ajout d'un objet à la position (9, 5)")

#montre sue l'on peut ajouter des objets sur la simu

add_objet(rob.simu.grille, Objet(), 9, 5)

print("\n\n - La grille aprés ajout\n\n")

affiche(rob.simu.grille)

print("\n\n - Génération d'une grille avec des obstacles pour les deplacement \n\n")

#pose des murs 
for i in range(1, len(rob.simu.grille)-1):
    for j in range(1, len(rob.simu.grille[0])-1):
        if randint(0, 10) == 0 and not isinstance(rob.simu.grille[i][j], RobotSimu):
            rob.simu.grille[i][j] = Wall()
        
affiche(rob.simu.grille)

#Demo de la vision du robot en fonction d'un angle

print("\n * Affichage de la vision selon un angle (une direction).\n\n \t 0 Est ► \n\n \t 90 sud ▼ \n\n \t 180 Ouest ◄ \n\n \t 270 Nord ▲ \n\n Et pour les autres direction on prend une valeur depuis l'interval")

ang = normalise_angle(int(input("\n - Donner une direction : ")))

print("\n - Voici la vision du robot suivant la direction :", ang, end="\n\n")

rob.simu.robot_simu.direction = ang
rob.simu.sync_vision()
affiche(rob.simu.vision.grille)

rob.simu.vision.libre_sur(1)

#Demo déplacemet du robot ( sans obstacles, juste montré qu'il peut se déplacer comme on veut ), ici il fera un carré

print("\n\n - Deplacement du robot : Dessin d'un carre : \n\n")

for i in range(1, len(rob.simu.grille)-1):
    for j in range(1, len(rob.simu.grille[0])-1):
        if not isinstance(rob.simu.grille[i][j], RobotSimu):
            rob.simu.grille[i][j] = None

affiche(rob.simu.grille)

input("Appuyer pour commencer ")

dist = 15

carre =  rob.deplace_robot(dist,0,40)
print("\n\n")

i = 0
while carre and i < 4:

    carre = rob.deplace_robot(dist,0,90)
    i += 1
    print("\n\n")


print("\n\n\n")

rob = Robot(16)
rob.set_simu(True)

#Demo detection d'obstacles 
#place des osbtacles sur la simu 

add_objet(rob.simu.grille, Wall(), 40, 40)
add_objet(rob.simu.grille, Wall(), 50, 50)
add_objet(rob.simu.grille, Wall(), 45, 45)

affiche(rob.simu.grille)
print("\n\n Avancer jusqu'a un obstacle \n\n")

input("Appuyer pour commencer ")
rob.deplace_robot(dist,0,40)