from Wall import Wall

def createGrille(larg, long):
	#retourne une grille de largeur larg et longueur long
	grille = []
        for x in range(0, larg):
            y = 0
            grille.append([])
            for y in range(0, long):
                grille[x].append(None)
        
        return grille
		
def affiche(grille):
	#affiche la grille en parametre
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
    
def is_Occupe(grille,x, y):
	#Permet de savoir si une case en position (x,y) de la grille est occupée ou non
        if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ):
     	    return grille[x][y] != None

        return False

def add_Objet(grille,objet, x, y):
	#ajoute un objet à la grille en parametre à la position (x,y)
        """Assuming objet is type Objet"""
        if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ) and ( Static.is_Occupe(grille,x,y) == False ) :
            grille[x][y] = objet
            return Static.is_Occupe(grille, x, y) #retourne False si l'action n'a pu se faire et True si l'action a réussi
        return False

    
