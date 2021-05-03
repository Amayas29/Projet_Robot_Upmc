from time import sleep
from datetime import datetime
from utils.tools import Vecteur, Point
from math import pi
from .obstacles import Balise


class Arene:

    def __init__(self):
        self.elements = []
        self.robot = None
        self.temps_precedent = None
        self.angle_parcouru = 0
        self.balise = None

    def boucle(self, fps):
        if self.robot is None:
            return

        while True:
            self.update()
            sleep(1./fps)

    def update(self):

        if self.temps_precedent is None:
            self.temps_precedent = datetime.now()

        now = datetime.now()
        diff_temps = (now - self.temps_precedent).total_seconds()
        self.temps_precedent = now

        if self.robot.lspeed == 0 and self.robot.rspeed == 0:
            return

        if self.robot.lspeed == self.robot.rspeed:

            angle_roue = diff_temps * self.robot.lspeed

            k = angle_roue // 360
            r = angle_roue % 360

            distance = k * self.robot.WHEEL_CIRCUMFERENCE + \
                (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

            self.robot.posr += angle_roue
            self.robot.posl += angle_roue

            x = self.robot.vec_deplacement.vect[0] * distance
            y = self.robot.vec_deplacement.vect[1] * distance

            point_tmp = Point(x, y)

            self.robot.center + point_tmp
            self.robot.refresh()
            return

        if self.robot.lspeed == 0 and self.robot.rspeed != 0:
            roue = Point.milieu(self.robot.chg, self.robot.chd)
            angle_roue = diff_temps * self.robot.rspeed
            self.robot.posr += angle_roue

        elif self.robot.rspeed == 0 and self.robot.lspeed != 0:
            roue = Point.milieu(self.robot.cbg, self.robot.cbd)
            angle_roue = diff_temps * self.robot.lspeed
            self.robot.posl += angle_roue

        k = angle_roue // 360
        r = angle_roue % 360

        distance = k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

        angle = distance * 180 / (pi * self.robot.WHEEL_BASE_WIDTH)

        if self.robot.lspeed == 0 and self.robot.rspeed != 0:
            angle = -angle

        self.angle_parcouru += angle
        self.robot.vec_deplacement = Vecteur.get_vect_from_angle(
            self.angle_parcouru)

        self.robot.center.rotate(roue, angle)
        self.robot.refresh()

    def set_robot(self, robot):
        if robot != None:
            self.robot = robot

    def add_obstacle(self, obstacle):
        if obstacle != None:
            self.elements.append(obstacle)

    def set_balise(self, balise):
        if balise != None and isinstance(balise, Balise):
            self.elements.append(balise)
            self.balise = balise
