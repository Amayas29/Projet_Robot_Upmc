import cv2
from math import atan2, degrees
from model.robot import Robot


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

    def color_profiles(self, n):
        if n == 0:
            name = "Bleu"
            hsv_lower = (95, 100, 20)
            hsv_upper = (115, 255, 255)
            return (name, hsv_lower, hsv_upper)

        if n == 1:
            name = "Rouge"
            hsv_lower = (0, 100, 50)
            hsv_upper = (10, 255, 255)
            return (name, hsv_lower, hsv_upper)

        if n == 2:
            name = "Vert"
            hsv_lower = (50, 100, 20)
            hsv_upper = (100, 255, 255)
            return (name, hsv_lower, hsv_upper)

        if n == 3:
            name = "Jaune"
            hsv_lower = (10, 100, 50)
            hsv_upper = (50, 255, 255)
            return (name, hsv_lower, hsv_upper)

    def get_masks_color(self, frame):
        masks = []

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        number = 0
        for i in range(4):
            _, hsv_lower, hsv_upper = self.color_profiles(i)
            mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
            mask = cv2.erode(mask, None, iterations=4)
            mask = cv2.dilate(mask, None, iterations=4)

            elements, _ = cv2.findContours(
                mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(elements) > 0:
                number += 1

            masks.append(mask)

        return masks, number

    def get_position_balise(self, frame):
        masks, number = self.get_masks_color(frame)

        if number < 3:
            return -1, -1

        mask = (masks[0] | masks[1]) | (masks[2] | masks[3])

        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)

        elements, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        c = max(elements, key=cv2.contourArea)

        ((x, y), _) = cv2.minEnclosingCircle(c)

        return x, y

    def get_angle_orientation_balise(self):

        if isinstance(self.robot, Robot):
            return self.robot.get_angle_orientation_balise()

        frame = self.robot.get_image()

        (x, y) = self.get_position_balise(frame)

        if x == -1:
            return -1, -1

        y = frame.shape[1] - y

        sign = x - (frame.shape[0] / 2)
        orientation = self.GAUCHE if sign < 0 else self.DROITE

        if y == 0:
            return 90, orientation

        angle = atan2(abs(sign), y)

        return degrees(angle), orientation
