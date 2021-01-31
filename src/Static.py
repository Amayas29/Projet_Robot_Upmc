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
        for ii in range(len(grille)*2):
            print("%-2s"%("-"),end=""),
        print("")
        for i in range(len(grille)):
            print("%-2s"%("|"),end=""),
            for j in range(len(grille[i])):
                print( "%-2s %-2s"%(str(grille[i][j]) , "|" ),end=""),
            print("")
            for jj in range(len(grille[i])*2):
                print("%-2s"%("-"),end=""),
            print("") 
