class Vision:

    def __init__(self, distance):
        self.distance = distance
        self.elements = []

    def check_collisions(self):
        return self.elements != []

    def sync_vision(self, robot, elements):
        pass
