class Static:
    @staticmethod
    def createGrille(larg, long):
        grille = []
        for x in range(0, larg):
            y = 0
            grille.append([])
            for y in range(0, long):
                grille[x].append(None)
        return grille

    @staticmethod
    def affiche(grille):
        """A changer, c'est pour afficher la memoire"""
        for x in range(0, len(grille)):
            print(str(grille[x]))    