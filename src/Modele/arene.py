class Arene:

    def __init__(self):
        self.elements = []
        self.robot = None


    def set_robot(robot):
        if robot != None:
            self.robot = robot


    def add_obstacle(obstacle):
        if obstacle != None:
            self.elements.append(obstacle)
