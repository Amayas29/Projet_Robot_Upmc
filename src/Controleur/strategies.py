class Action:

    def __init__(self, name, robot):
        self.name = name
        self.is_stop = False
        self.robot = robot


    def run(self, vision):
        pass

class Avancer(Action):

    def __init__(self, robot, distance, vitesse):
        super().__init__("Avancer", robot)
        self.distance = distance
        self.distance_parcouru = 0
        self.vitesse = vitesse


    def run(self, vision):
        
        if self.distance_parcouru >= self.distance or vision.check_collisions():
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)
            self.is_stop = True
            return
        
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, self.vitesse)
        

class Strategie:

    def __init__(self, robot):
        self.current_action = -1
        self.actions = []
        self.robot  = robot


    def start(self):
        if self.actions != []:
            self.current_action = 0
            for action in self.actions:
                action.is_stop = False


    def stop(self):
        self.current_action = len(self.actions)

    
    def is_stop(self):
        return self.current_action >= len(self.actions)


    def is_start(self):
        return self.current_action > 0


    def add_action(self, action):
        self.actions.append(action)


    def run(self, vision):

        if not self.is_start():
            self.start()
        
        if self.actions[self.current_action].is_stop:
            self.current_action += 1

        if not self.is_stop() and self.is_start():
            self.actions[self.current_action].run(self.robot, vision)
            