from math import *

def create_grille(larg, long):
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
    

def is_occupe(grille,x, y):
#Permet de savoir si une case en position (x,y) de la grille est occupée ou non
    if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ):
 	    return grille[x][y] != None

    return False


def add_objet(grille,objet, x, y):
	#ajoute un objet à la grille en parametre à la position (x,y)
    """Assuming objet is type Objet"""
    if ( 0 <= x < len(grille) ) and ( 0 <= y < len(grille[0]) ) and (is_occupe(grille,x,y) == False ) :
        grille[x][y] = objet
        return is_occupe(grille, x, y) #retourne False si l'action n'a pu se faire et True si l'action a réussi
    return False

# # Pour les tests : Je la garde pour explique en Vocal au groupe
# def add_objet(grille,objet, x, y):
#     grille[x][y] = str(objet) + "9"


def to_radian(ang):
    """
        float -> float
        Transforme un angle de degree en radian
    """
    return (ang * pi) / 180


def to_degree(ang):
    """
        float -> float
        Transforme un angle de radian en degree
    """
    return (ang * 180) / pi


def get_vect_from_angle(ang):
    """
        float -> Tuple
        Construit un vecteur direction depuis un angle donné
    """
    ang = to_radian(ang)
    return (round(cos(ang), 2), round(sin(ang), 2))


def get_vect_from_points(src_point, dest_point):
    """
        Tuple * Tuple -> Tuple
        Construit un vecteur entre un point source vers un point destination
    """
    return (dest_point[0] - src_point[0], dest_point[1] - src_point[1])


def produit_scalaire(vec1, vec2):
    """
        Tuple * Tuple -> float
        Calcule le produit scalaire de deux vecteur
    """
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def norme(vec):
    """
        Tuple -> float
        Calcule la norme d'un vecteur
    """
    return sqrt(vec[0]**2 + vec[1] ** 2)


def angle(vec1, vec2):
    """
        Tuple * Tuple -> float
        Calcule l'angle entre deux vecteur (sans prendre en consideration l'orientation)
        Hyp les vecteurs doivent pas etre null
    """
    norme_ = norme(vec1) * norme(vec2)
    return round(to_degree(acos(produit_scalaire(vec1, vec2) / norme_)),2)


def __sign__(vec1, vec2):
    """
        Tuple * Tuple -> float
        Permet de savoir le signe de l'angle entre les vecteurs
    """
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def angle_sign(vec1, vec2):
    """
        Tuple * Tuple -> float
        Retourne l'angle signe entre les deux vecteurs
    """
    ang = angle(vec1, vec2)
    return ang if __sign__(vec1, vec2) >= 0 else - ang


def in_vision(vec_src, new_vec):
    """
        Tuple * Tuple -> bool
        Permet de savoir si l'angle entre les vecteur est inferieur à 90 pour delimiter un demi plan
    """
    return angle(vec_src, new_vec) <= 90


def distance(droite, point):
    """
        Tuple * Tuple -> float
        Calcule la distance entre une droite et un point
    """
    return abs(droite[0] * point[0] + droite[1] * point[1] + droite[2]) / (sqrt(droite[0] ** 2 + droite[1] ** 2))


def __get_milieu__(p1, p2):
    """
        Tuple * Tuple -> Tuple
        Retourne le milieu d'un segment de deux points (A l'entier superieur)
    """
    return (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))


def __get_carre__(taille, x, y):
    """
        int * int * int -> (int * int * int * int)
        Permet de retourne les indices du haut, gauche, bas et de droite d'un carre
    """

    pair = taille % 2
    g = x - int(taille/2)
    d = x + int(taille/2) + pair - 1
    h = y - int(taille/2)
    b = y + int(taille/2) + pair - 1

    return (h, g, b, d)


def normalise_angle(ang):
    """
        float -> float
        Permet de rendre un angle entre 0 et 360
    """
    return ang % 360


def get_src_point(taille, x, y, ang):
    """
        int * int * int * float -> Tuple
        construit le point source sortant du carre
    """

    ang = normalise_angle(ang)

    (ht, gch, bs, dte) = __get_carre__(taille, x, y)

    a = (gch, ht)
    b = (dte, ht)
    c = (gch, bs)
    d = (dte, bs)

    if ang == 0:
        return __get_milieu__(b, d)

    elif ang == 90:
        return __get_milieu__(c, d)

    elif ang == 180:
        return __get_milieu__(a, c)

    elif ang == 270:
        return __get_milieu__(a, b)

    elif 0 < ang < 90:
        return d

    elif 90 < ang < 180:
        return c

    elif 180 < ang < 270:
        return a

    elif ang > 270:
        return b