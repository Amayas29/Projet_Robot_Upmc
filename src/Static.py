from Wall import Wall

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
        #Creation d'une grille
        print("|",end="")
        print("%-2s"%("-"),end="")
        for i in range(len(grille)-1):
            print("%-3s"%("-"),end="")
        print("|")        
        for i in range(len(grille[0])):
            
            for j in range(len(grille)):
                print("|",end="")
                if grille[j][i] == None:
                    print("%-2s"%(" "),end="")
                else:
                    print("%-2s"%(grille[j][i]),end="")
		
            print("|")
            print("|",end="")
            print("%-2s"%("-"),end="")

            for i in range(len(grille)-1):
                print("%-3s"%("-"),end="")
     
            print("|")
    
    @staticmethod
    def is_Occupe(grille,x, y):
        if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ):
     	    return grille[x][y] != None

        return False

    @staticmethod
    def add_Objet(grille,objet, x, y):
        """Assuming objet is type Objet"""
        if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ) and ( Static.is_Occupe(grille,x,y) == False ) :
            grille[x][y] = objet
            return Static.is_Occupe(grille, x, y)
        return False

    
