from time import sleep


class ImageLoader:

    def __init__(self, robot):
        self.robot = robot
        self.image = None
        self.run = True

    def boucle(self, fps):

        while self.run:
            self.image = self.robot.get_image()
            sleep(1./fps)

    def stop(self):
        self.run = False

    def get_image(self):
        return self.image
