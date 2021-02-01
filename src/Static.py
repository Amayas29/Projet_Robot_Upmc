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
        
        for ii in range(0, larg):
            for j in range(0,long):
                grille[0][j] = Wall()
                grille[len(grille) - 1][j] = Wall()
                grille[j][0] = Wall()
                grille[j][len(grille[ii]) - 1] = Wall()
        return grille

    @staticmethod
    def affiche(grille):
        #Creation d'une grille
        print("|",end="")
        print("%-2s"%("-"),end="")
        for i in range(len(grille)-1):
            print("%-3s"%("-"),end="")
        print("|")        
        for i in range(len(grille)):
            
            for j in range(len(grille[0])):
                print("|",end="")
                if grille[i][j] == None:
                    print("%-2s"%(" "),end="")
                else:
                    print("%-2s"%(grille[i][j]),end="")

                
            print("|")
            print("|",end="")
            print("%-2s"%("-"),end="")

            for i in range(len(grille)-1):
                print("%-3s"%("-"),end="")
       

            print("|")
    
    @staticmethod
    def is_Occupe(grille,x, y):
    	if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ):
     	   return grille[x][y]!=None
     	return False

    @staticmethod
    def add_Objet(grille,objet, x, y):
        """Assuming objet is type Objet"""
        if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ) and ( Static.is_Occupe(grille,x,y) == False ) :
            grille[x][y] = objet
            return Static.is_Occupe(grille, x, y)
        return False

    
