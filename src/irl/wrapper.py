from .vision import Vision


class Wrapper:

    def __init__(self, robot):
        self.robot = robot
        self.vision = Vision()

    def stop(self):
        self.robot.stop()
