import sys
sys.path.append(..)
import random
from math import *
from src.utils.tools import *
import unittest

class TestTools(unittest.TestCase):

    def setUp(self):
        self.p = Point(1,2)
        self.p2 = Point(2,3)
        self.v = Vecteur(3,4)
        self.v2 = Vecteur(4,5)
        self.s = Segment(4,5)
        self.s2 = Segment(3,4)
        self.d = Droite(1,2,3)
        

    def tests_Point(self):
        self.assertEqual(self.p.add(Point(1,2)),Point(2,4))
        self.assertEqual(self.p.__sub__(Point(1,2)),0)
        self.assertEqual(self.p.distance_to_droite(self.d),8/sqrt(5))
        self.assertEqual(self.p.rotate(Point(2,2),90),Point(2,3))
        self.assertEqual(Point.milieu(self.p,self.p2),Point(3/2,5/2))
        self.assertEqual(Point.get_point_distance(self.p,self.v,2),(Point(-1,9/2),Point(3,1/2)))

    def tests_Vecteur(self):
        self.assertEqual(self.v.__mul__(v2),32)
        self.assertEqual(self.v.norme(),5)
        self.assertNotEqual(self.v.angle(self.v2),0)
        self.assertEqual(self.v.sign(self.v2),-1)
        self.assertEqual(self.v.angle_sign(self.v2),self.angle(self.v2))

    def tests_droite(self):
        self.assertEqual(Droite.get_droite(self.v,self.p),Droite(3,4,-11))
        self.assertNotEqual(Droite.intersection(self.v,self.p1,self.v2,self.p2),Point(10,12))

    def tests_seg(self):
        self.assertTrue(self.s.intersection(self.p,self.v))
        self.assertEqual(self.s.to_droite(),Droite.get_droite(Point(0,0),Point(-5,4),(-4*Point(0,0)-Point(-5,4)*(-4))
        self.assertEqual(self.s.distance_to_droite(self.s2),self.s2.src.distance_to_droite(self.s.to_droite))

if __name__ == '__main__':
    unittest.main()