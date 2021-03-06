from math import radian, degrees, sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance_point(self, other):
        """
        Retourne la distance entre 2 points
        """
        return sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )


    def distance_droite(self, droite):
        """
        Retourne la distance entre le point courrant et une doite
        """
        return abs(droite[0] * self.x + droite[1] * self.y + droite[2]) / (sqrt(droite[0] ** 2 + droite[1] ** 2))

    
    def rotation(self, angle):
        pass


class Vecteur:

    def __init__(self, src, dest):
        self.vect = (dest.x - src.x, dest.y - src.y)
    

    @staticmethod
    def get_vect_from_angle(ang):
        """
        Construit un vecteur direction depuis un angle donné
        """
        ang = radian(ang)
        return Vecteur(Point(0, 0), Point(round(cos(ang), 2), round(sin(ang), 2)))


    def __mul__(self, other):
        """
        Calcule le produit scalaire de deux vecteur
        """
        return self.vect[0] * other.vect[0] + self.vect[1] * other.vect[1]


    def norme(self):
        """
        Calcule la norme d'un vecteur
        """
        return sqrt(self.vect[0]**2 + self.vect[1] ** 2)


    def angle(self, other):
        """
        Calcule l'angle entre deux vecteur (sans prendre en consideration l'orientation)
        """
        norme_ = self.norme() * other.norme()
        if(norme_ == 0):
            return 0
        return round(degrees(acos(round((self * other) / norme_, 5))),2)


    def sign(self, other):
        """
        Permet de savoir le signe de l'angle entre les vecteurs
        """
        return self.vect[0] * other.vect[1] - self.vect[1] * other.vect[0]


    def angle_sign(self, other):
        """
        Retourne l'angle signe entre les deux vecteurs
        """
        ang = self.angle(other)
        return ang if self.sign(other) >= 0 else - ang