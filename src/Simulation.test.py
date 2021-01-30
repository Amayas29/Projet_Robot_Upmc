import random
import Simulation

def testCreateGrille():
    for _ in range(100):
        random_largeur = random.randint(1, 2000)
        random_longueur = random.randint(1, 2000)

        grille = Simulation.Simulation.createGrille(random_largeur, random_longueur)

        assert random_largeur == len(grille)
        assert all(len(line) == random_longueur for line in grille)

    for i in range(-50, 1):
        grille = Simulation.Simulation.createGrille(i, i)
        assert 0 == len(grille)


if __name__ == '__main__':
    try:
        testCreateGrille()
        print("Test: Create Grille successful")
    except AssertionError as e:
        print(e)
