from abc import abstractmethod


class Strategie(object):

    def __init__(self, robot):
        self.robot = robot
        self.is_stop = False
        self.is_start = False
        self.old_position = None

    def start(self):
        self.is_stop = False
        self.is_start = True

    def stop(self):
        self.robot.stop()
        self.is_stop = True

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
        self.robot.stop()
        self.old_position = self.robot.get_motor_position()[0]
        self.robot.servo_rotate(90)
        self.distance_parcouru = 0

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        diff = self.robot.get_motor_position()[0] - self.old_position
        self.old_position = self.robot.get_motor_position()[0]

        k = diff // 360
        r = diff % 360

        self.distance_parcouru += k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de avancer __dist__ :", self.distance_parcouru,
                  self.robot.get_distance())
            return
      
        if self.robot.get_distance() <= 150:
            self.robot.stop()
            print("Arret de avancer __collid__ :", self.distance_parcouru,
                  self.robot.get_distance())
            return

        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, self.vitesse)


class Tourner(Strategie):

    GAUCHE = 1
    DROITE = 0

    def __init__(self, robot, angle, orientation, vitesse):
        super().__init__(robot)
        if orientation != self.DROITE and orientation != self.GAUCHE:
            orientation = self.GAUCHE
        self.orientation = orientation
        self.vitesse = vitesse
        self.distance = (robot.WHEEL_BASE_CIRCUMFERENCE * angle) / 180
        self.distance_parcouru = 0
        self.ralentir = 1

    def start(self):
        super().start()
        self.robot.stop()
        self.old_position = self.robot.get_motor_position()[
            self.orientation]

        self.distance_parcouru = 0

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.orientation == self.GAUCHE:
            self.robot.servo_rotate(60)
        else:
            self.robot.servo_rotate(110)

        diff = self.robot.get_motor_position()[self.orientation] - \
            self.old_position

        self.old_position = self.robot.get_motor_position()[self.orientation]

        k = diff // 360
        r = diff % 360

        self.distance_parcouru += k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de tourner __dist__ :", self.distance_parcouru,
                  self.robot.get_distance())
            return

        if self.robot.get_distance() <= 150:
            self.robot.stop()
            print("Arret de tourner __collid__ :", self.distance_parcouru,
                  self.robot.get_distance())
            return
        if self.distance_parcouru < self.distance /2:
            self.ralentir = 2
        elif self.distance_parcouru < self.distance *3/4:
            self.ralentir = 3

        if self.orientation == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.vitesse/self.ralentir)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  self.vitesse/self.ralentir)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)
    
        
          

class Carre(Strategie):

    NB_MAX = 8

    def __init__(self, robot, cote, vitesse, orientation):
        super().__init__(robot)
        self.avancer = Avancer(robot, cote, vitesse)
        self.tourner = Tourner(robot, 90, orientation, vitesse)
        self.cur = -1
        self.nb = 0

    def start(self):
        super().start()
        self.cur = 0
        self.nb = 0
        self.avancer.start()

    def stop(self):
        super().stop()
        self.cur = -1

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.nb == self.NB_MAX:
            self.stop()
            return

        if self.cur == 0:

            if not self.avancer.is_stop:
                self.avancer.run()
            else:
                self.cur = 1
                self.nb += 1
                self.tourner.start()

        else:

            if not self.tourner.is_stop:
                self.tourner.run()
            else:
                self.cur = 0
                self.nb += 1
                self.avancer.start()

class Triangle(Strategie):

    NB_MAX = 6

    def __init__(self, robot, cote, vitesse, orientation):
        super().__init__(robot)
        self.avancer = Avancer(robot, cote, vitesse)
        self.tourner = Tourner(robot, 120, orientation, vitesse)
        self.cur = -1
        self.nb = 0

    def start(self):
        super().start()
        self.cur = 0
        self.nb = 0
        self.avancer.start()

    def stop(self):
        super().stop()
        self.cur = -1

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.nb == self.NB_MAX:
            self.stop()
            return

        if self.cur == 0:

            if not self.avancer.is_stop:
                self.avancer.run()
            else:
                self.cur = 1
                self.nb += 1
                self.tourner.start()

        else:

            if not self.tourner.is_stop:
                self.tourner.run()
            else:
                self.cur = 0
                self.nb += 1
                self.avancer.start()


class EviterObstacle(Strategie):

    def __init__(self ,robot,vitesse,distance,angle,securite):
        super().__init__(robot)
        self.avancer = Avancer(self.robot,distance,vitesse)
        self.tourner = Tourner(self.robot,angle,Tourner.DROITE,vitesse)
        self.collid = False
        self.securite = securite

    def start(self):
        super().start()
        self.collid = False
        self.avancer.start()

    def stop(self):
        super().stop()
        self.avancer.stop()
        self.tourner.stop()
    
    def run(self):
        if self.is_stop:
            return
        
        if not self.is_start:
            self.start()
        
        if self.collid:
            self.tourner.run()
            return
        print(self.robot.get_distance())

        if self.robot.get_distance() <= self.securite:
            self.tourner.start()
            print("collision detecter",self.robot.get_distance(), self.securite)
            self.robot.servo_rotate(20)
            if self.robot.get_distance() <= self.securite:
                self.tourner.orientation = Tourner.GAUCHE
            self.collid = True
            self.tourner.start()
            return
        else:
            if not self.avancer.is_start:
                self.avancer.start()
            self.collid = False
        
        self.avancer.run()