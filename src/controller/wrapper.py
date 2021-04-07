
class Wrapper(object):

    GAUCHE = 1
    DROITE = 0

    def __init__(self, robot):
        self.robot = robot
        self.liste_ref = {}
        self.WHEEL_BASE_CIRCUMFERENCE = robot.WHEEL_BASE_CIRCUMFERENCE

    def begin(self, ref, port):
        self.liste_ref[ref] = self.robot.get_motor_position()[port]

    def get_distance_parcouru(self, ref, port):

        diff = self.robot.get_motor_position()[port] - self.liste_ref[ref]
        self.liste_ref[ref] = self.robot.get_motor_position()[port]

        k = diff // 360
        r = diff % 360

        return k * self.robot.WHEEL_CIRCUMFERENCE + \
            (r * self.robot.WHEEL_CIRCUMFERENCE) / 360

    def avancer(self, vitesse):
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, vitesse)

    def stop(self):
        self.robot.stop()

    def tourner_servo(self, angle):
        self.robot.servo_rotate(angle)

    def get_distance(self):
        return self.robot.get_distance()

    def tourner(self, cote, vitesse):
        if cote == self.GAUCHE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, vitesse)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, vitesse)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)
