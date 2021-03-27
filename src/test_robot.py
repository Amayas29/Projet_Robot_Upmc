import random
from modele.robot import Robot
import math
import unittest

class RobotTest(unittest.TestCase):

    def setUp(self):
      # premier robot : r1
      self.center = (random.uniform(-50, 50), random.randint( 0 , 50 ))
      self.random_longueur = random.randint(0, 50)
      self.random_largeur = random.randint(0, 50)
      self.random_vitesse = random.uniform(-50, 50)
      self.r1 = Robot(self.center, self.random_longueur , self.random_largeur, self.random_vitesse)
      # deuxieme robot : r2 
      self.v2 = random.randint(50 , 100)
      self.lo2 = random.uniform(-50, 50)
      self.la2 = random.uniform(-50, 50)
      self.r2 = Robot(self.c2, self.lo2, self.la2 , self.random_vitesse)
      # troisieme robot : r3
      self.r3 = Robot(self.c2 , self.lo2 , self.la2, 0.)

    def test_rotation(self):
        r = Robot(0., 0., 1., 0.)
        oldAngle = 0
        oldVecteurD = r.vec_deplacement
        deltaT = random.uniform(0, 5)
        randomAngleRelative = r._degreParSeconde * deltaT
        r.rotation(deltaT)

        self.assertTrue(abs(oldAngle - r.angle) == randomAngleRelative)

        compare_vecteur = r.vecteurDeplacement + oldVecteurD.rotation(randomAngleRelative) * (-1)
        self.assertTrue(abs(compare_vecteur.norme()) < 0.00001)


    def test_avance(self):
        # cas particuliers d'immobilité
        temps = random.randint(1, 100)
        pos_x_init = random.uniform(-50, 50)
        pos_y_init = random.uniform(-50, 50)
        vitesse = random.uniform(-10, 10)
        angle = random.uniform(-180, 180)
        # cas d'une vitesse nulle => immobile
        r = Robot.Robot(pos_x_init, pos_y_init, 0., angle)
        r.avance(temps)
        self.assertTrue(r.x == pos_x_init)
        self.assertTrue(r.y == pos_y_init)
        # cas d'un temps null => immobile
        r = Robot(pos_x_init, pos_y_init, vitesse, angle)
        r.avance(0)
        self.assertTrue(r.x == pos_x_init)
        self.assertTrue(r.y == pos_y_init)

        # cas général, en prenant en compte l'incertitude de calcul --> float (arrondis au 1e-10 pres)
        for _ in range(1000):
            temps = random.randint(1, 100)
            pos_x_init = random.uniform(-50, 50)
            pos_y_init = random.uniform(-50, 50)
            vitesse = random.uniform(-10, 10)
            angle = random.uniform(-180, 180)
            r = Robot.Robot(pos_x_init, pos_y_init, vitesse, angle)
            r.avance(temps)
            pos_x_fin = pos_x_init + ((math.cos(math.radians(angle)) * vitesse) * temps)
            pos_y_fin = pos_y_init + ((math.sin(math.radians(angle)) * vitesse) * temps)
            # ordre de grandeur de l'incertitude = 0,0000000001 prés
            ordre_grandeur = 10 ** -10
            self.assertTrue(abs(r.x - pos_x_fin) < ordre_grandeur)  # test que valeurs identiques a 1e-10 prés
            self.assertTrue(abs(r.y - pos_y_fin) < ordre_grandeur)  # test que valeurs identiques a 1e-10 prés



print ("Yees")