from Utils.tools import Point, Vecteur

class Robot:

    def __init__(self, center, longeur, largeur, vitesse):

        self.center = center
        self.longeur = longeur
        self.largeur = largeur

        self.chg = Point(center.x - longeur//2, center.y + largeur//2)
        self.cbg = Point(center.x - longeur//2, center.y - largeur//2)

        self.chd = Point(center.x + longeur//2, center.y + largeur//2)
        self.cbd = Point(center.x + longeur//2, center.y - largeur//2)

        self.angle = 0
        self.vitesse = vitesse


    def forward(self):
        """
        Permet de bouger le robot d'une case en suivant ca direction
        """
        
        angle = self.angle % 360
        vict = Vecteur.get_vect_from_angle(angle)
       
        self.chg += vict.vict
        self.chd += vict.vict
        self.cbg += vict.vict
        self.cbd += vict.vict
        self.center += vict.vict
        
        
    def start(self, vitesse):
        pass
    
    def stop(self):
        pass

    
    def tourne(self, angle):
        """
        Permet de tourner le robot 
        """
        angle = angle % 360
        self.angle = angle
        self.chg.rotation(self.center, angle)
        self.chd.rotation(self.center,angle)
        self.cbg.rotation(self.center,angle)
        self.cbd.rotation(self.center,angle)
      
    