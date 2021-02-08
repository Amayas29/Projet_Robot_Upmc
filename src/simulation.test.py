import random
from tool import *

#classe teste de la Simulation
def test_create_grille():
    """
        Test de creation des grilles et des affichage
    """
    
    #teste aléatoirement le bon fonctionnement de la méthode
    for _ in range(10):

        random_largeur = random.randint(1, 30)
        random_longueur = random.randint(1, 30)

        grille = create_grille(random_largeur, random_longueur)

        assert random_largeur == len(grille)
        assert all(len(line) == random_longueur for line in grille)

        affiche(grille)
        print("")
        input("Appuyer pour entrer pour passer à la grille suivante ...")
        print("")

    # Test avec des dimension négative, la grille sera vide
    grille = create_grille(-4, -7)
    assert 0 == len(grille)


if __name__ == '__main__':
    #main qui test si le test est réussi ou non =)
    try:
        test_create_grille()
        print("Test: Create Grille successful")
    except AssertionError as e:
        print(e)
