import random
from Static import *

#classe teste de la Simulation
def testCreateGrille():
    """
        Test de creation des grilles et des affichage
    """
    for _ in range(10):

        random_largeur = random.randint(1, 30)
        random_longueur = random.randint(1, 30)

        grille = Static.createGrille(random_largeur, random_longueur)

        assert random_largeur == len(grille)
        assert all(len(line) == random_longueur for line in grille)

        Static.affiche(grille)
        print("")
        input("Appuyer pour entrer pour passer à la grille suivante ...")
        print("")

    # Test avec des dimension négative, la grille sera vide
    grille = Static.createGrille(-4, -7)
    assert 0 == len(grille)


if __name__ == '__main__':
    #main qui test si le test est réussi ou non =)
    try:
        testCreateGrille()
        print("Test: Create Grille successful")
    except AssertionError as e:
        print(e)
