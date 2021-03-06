from Utils import Point

class Robot:

    def __init__(self, center, longeur, largeur, angle, vitesse):

        self.center = center
        self.longeur = longeur
        self.largeur = largeur

        self.chg = Point(center.x - longeur//2, center.y - largeur//2)
        self.chd = Point(center.x - longeur//2, center.y + largeur//2)
        self.cbg = Point(center.x - longeur//2, center.y + largeur//2)
        self.cbd = Point(center.x + longeur//2, center.y + largeur//2)

        self.angle = angle
        self.vitesse = vitesse

        
    def start(self, vitesse):
        pass

    
    def stop(self):
        pass

    
    def tourne(self, angle):
        pass