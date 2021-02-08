from vision import Vision
from tool import *
from wall import Wall

#test le fonctionnement de la vision
def test_add_objet(vision):
    #ajoute des Wall aux à certaines positions
    print(add_objet(vision.grille,Wall(),2,3))
    print(add_objet(vision.grille,Wall(),2,3))
    print(add_objet(vision.grille,Wall(),3,2))


if __name__ == '__main__':
    v = Vision(10, 10, 1) #grille de 10*10
    try:
        #essaye de
        test_add_objet(v) # ajouter les murs
        affiche(v.grille) #affiche la vision
        print("\nTest: Add Objet successful")

    except AssertionError as e:
        print(e)
