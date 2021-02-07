from Vision import Vision
from Tool import *
from Wall import Wall

# vis = Vision(9*4,9*4,int(9*0.25))

# for i in range(len(vis.grille)):
#     vis.grille[3][i] = Wall()
#     vis.libresur(4)
#     print(i)
#     vis.grille[3][i] = None

for i in range(len(vis.grille)):
    vis.grille[3][i] = Wall()
    vis.libresur(1)
    print(i)
    vis.grille[3][i] = None



for i in range(vis.long//2 - vis.tailleRob//2,vis.long//2 + vis.tailleRob//2):
    vis.grille[i][0] = "R"

affiche(vis.grille)