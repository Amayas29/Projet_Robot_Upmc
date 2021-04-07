import random
from model.robot import Robot
import math
import unittest


class RobotTest(unittest.TestCase):

    def setUp(self):
        # premier robot : r1
        self.center = (random.uniform(-50, 50), random.randint(0, 50))
        self.random_vitesse = random.uniform(-50, 50)
        self.r1 = Robot(self.center, self.random_vitesse)
        # deuxieme robot : r2
        self.v2 = random.randint(50, 100)
        self.r2 = Robot(self.c2, self.random_vitesse)
        # troisieme robot : r3
        self.r3 = Robot(self.c2, 0.)

    # def test_rotation(self):
    #     r = Robot(0., 0.)
    #     oldAngle = 0
    #     oldVecteurD = r.vec_deplacement
    #     deltaT = random.uniform(0, 5)
    #     randomAngleRelative = r._degreParSeconde * deltaT
    #     r.rotation(deltaT)

    #     self.assertTrue(abs(oldAngle - r.angle) == randomAngleRelative)

    #     compare_vecteur = r.vecteurDeplacement + \
    #         oldVecteurD.rotation(randomAngleRelative) * (-1)
    #     self.assertTrue(abs(compare_vecteur.norme()) < 0.00001)

    # def test_avance(self):
    #     pass
