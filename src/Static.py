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
        for ii in range(len(grille)*2):
            print("-"),
        print("")
        for i in range(len(grille)):
            print("|"),
            for j in range(len(grille[i])):
                print( str(grille[i][j]) + " |" ),
            print("")
            for jj in range(len(grille[i])*2):
                print("-"),
            print("")  
