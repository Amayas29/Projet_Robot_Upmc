from time import sleep
from datetime import datetime
from utils.tools import Vecteur, Point
from math import pi


class Arene:

    def __init__(self):
        self.elements = []
        self.robot = None
        self.temps_precedent = datetime.now()

    def boucle(self, fps):
        if self.robot is None:
            return

        while True:
            self.update()
            sleep(1./fps)

    def update(self):
        diff_temps = (datetime.now() - self.temps_precedent).total_seconds()
        self.temps_precedent = datetime.now()

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

            self.robot.chg + point_tmp
            self.robot.cbg + point_tmp
            self.robot.chd + point_tmp
            self.robot.cbd + point_tmp

        elif self.robot.lspeed == 0 and self.robot.rspeed != 0:
            roue = Point((self.robot.chg.x + self.robot.chd.x)/2,
                         (self.robot.chg.y + self.robot.chd.y)/2)
            angle_roue = diff_temps * self.robot.rspeed
            distance = angle_roue * (self.robot.WHEEL_CIRCUMFERENCE / 360)

            self.robot.posr += angle_roue

            angle = distance/((pi * (self.robot.chd - self.robot.cbd))/180)
            self.robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)

            self.robot.chg.rotate(roue, angle)
            self.robot.cbg.rotate(roue, angle)
            self.robot.chd.rotate(roue, angle)
            self.robot.cbd.rotate(roue, angle)

        elif self.robot.rspeed == 0 and self.robot.lspeed != 0:
            roue = Point((self.robot.cbg.x + self.robot.cbd.x)/2,
                         (self.robot.cbg.y + self.robot.cbd.y)/2)

            angle_roue = diff_temps * self.robot.lspeed
            distance = angle_roue * (self.robot.WHEEL_CIRCUMFERENCE / 360)

            self.robot.posl += angle_roue

            angle = distance/((pi * self.robot.chd - self.robot.cbd)/180)
            self.robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)

            self.robot.chg.rotate(roue, angle)
            self.robot.cbg.rotate(roue, angle)
            self.robot.chd.rotate(roue, angle)
            self.robot.cbd.rotate(roue, angle)

        # TODO
        elif self.robot.lspeed > self.robot.rspeed:
            pass
        elif self.robot.lspeed < self.robot.rspeed:
            pass
        else:
            pass

    def set_robot(self, robot):
        if robot != None:
            self.robot = robot

    def add_obstacle(self, obstacle):
        if obstacle != None:
            self.elements.append(obstacle)
