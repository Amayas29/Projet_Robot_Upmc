from vision import Vision
from tool import *
from wall import Wall

#tests de la nouvelle méthode libresur
vis = Vision(9*4,9*4,int(9*0.25))

# for i in range(len(vis.grille)):
#     vis.grille[3][i] = Wall()
#     vis.libre_sur(4)
#     print(i)
#     vis.grille[3][i] = None

for i in range(len(vis.grille)):
    vis.grille[3][i] = Wall()
    vis.libre_sur(1)
    print(i)
    vis.grille[3][i] = None

#parcours une grille et test si les cases sont libres

for i in range(vis.long//2 - vis.taille_rob//2,vis.long//2 + vis.taille_rob//2):
    vis.grille[i][0] = "R"

affiche(vis.grille)