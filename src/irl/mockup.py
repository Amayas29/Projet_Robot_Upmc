import math


class Robot2I013Mockup(object):

    WHEEL_BASE_WIDTH = 117
    WHEEL_DIAMETER = 66.5
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi

    def __init__(self, fps=25, resolution=None, servoPort="SERVO1", motionPort="AD1"):
        self.MOTOR_LEFT = 0
        self.MOTOR_RIGHT = 0

    def set_led(self, led, red=0, green=0, blue=0):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        pass

    def get_motor_position(self):
        return (0, 0)

    def offset_motor_encoder(self, port, offset):
        pass

    def get_distance(self):
        return 10

    def servo_rotate(self, position):
        pass

    def stop(self):
        pass

    def get_image(self):
        pass
