import math


class Robot2I013Mockup(object):

    WHEEL_BASE_WIDTH = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER = 66.5  # diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * \
        math.pi  # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi  # perimetre de la roue (mm)

    def __init__(self, controler, fps=25, resolution=None, servoPort="SERVO1", motionPort="AD1"):
        pass

    def set_led(self, led, red=0, green=0, blue=0):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        pass

    def get_motor_position(self):
        pass

    def offset_motor_encoder(self, port, offset):
        pass

    def get_distance(self):
        pass

    def servo_rotate(self, position):
        pass

    def stop(self):
        pass

    def get_image(self):
        pass
