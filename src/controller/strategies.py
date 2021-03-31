from math import pi
from abc import abstractmethod


class Strategie(object):

    def __init__(self, robot):
        self.robot = robot
        self.is_stop = False
        self.is_start = False

    def start(self):
        self.is_stop = False
        self.is_start = True

    def stop(self):
        self.is_stop = True
        self.is_start = False

    @abstractmethod
    def run(self):
        pass


class Avancer(Strategie):

    def __init__(self, robot, distance, vitesse):

        super().__init__(robot)
        self.distance = distance
        self.distance_parcouru = 0
        self.vitesse = vitesse

    def start(self):
        super().start()
        self.robot.offset_motor_encoder(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)
        self.robot.servo_rotate(90)

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        diff = self.robot.get_motor_position()[0]

        k = diff // 360
        r = diff % 360

        self.distance_parcouru += k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

        if self.distance_parcouru >= self.distance or self.robot.get_distance() <= 5:
            self.robot.stop()
            self.stop()
            print("Arret de avancer")
            return

        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, self.vitesse)


class Tourner(Strategie):

    GAUCHE = 1
    DROITE = 0
    def __init__(self, robot, angle, orientation,vitesse):
        super().__init__(robot)
        self.angle = angle
        self.angle_parcouru = 0
        self.orientation = orientation
        self.vitesse = vitesse
        self.distance_a_parcourire = 2 * PI * robot.WHEEL_BASE_WIDTH * angle / 360
        self.distance_parcouru = 0

    def start(self):
        super().start()
        self.robot.offset_motor_encoder(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)

        if self.orientation == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.angle)
        elif self.orientation == self.DROITE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  self.angle)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        # Calcule de l'angle_parcouru

        if self.orientation == self.GAUCHE:
            diff = self.robot.get_motor_position()[0]
        elif self.orientation == self.DROITE:
            diff = self.robot.get_motor_position()[1]
        

        k = diff // 360
        r = diff % 360

        self.distance_parcouru += k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360
       
        if self.robot.get_distance() <= 5 and self.distance_parcouru != self.distance_a_parcourire:
            self.robot.stop()
            self.stop()
            print("Arret de tourner")
            return

        if self.orientation == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.vitesse)
        elif self.orientation == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  self.vitesse)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)



class Carre(Strategie):

    def __init__(self,robot):
        self.avancer = Avancer(robot,)
        self.tourner = Tourner()
        self.stop()

    def start(self):
        super().start()
        self.cur = 0
        self.nb = 0
    
    def stop(self):
        super().stop()
        self.cur = -1
        self.nb = 0

    def run():
        
