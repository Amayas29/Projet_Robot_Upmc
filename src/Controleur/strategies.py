class Action:

    def __init__(self, name, vitesse):
        self.name = name
        self.vitesse = vitesse

    def run(self, robot):
       pass


class Avancer(Action):

    def __init__(self):
        super().__init__("Avancer")

    def run(self, robot):
        robot.set_vitesse(self.vitesse)
    

class Strategie:

    def __init__(self, robot):
        self.current_action = -1
        self.actions = []
        self.robot  = robot


    def start(self):
      if self.action != []:
        self.current_action = 0


    def stop(self):
        self.current_action = len(self.actions)

    
    def is_stop(self):
        return self.current_action >= len(self.actions)


    def is_start(self):
        return self.current_action > 0


    def add_action(self, action):
        self.actions.append(action)

    def run(self):

        if not self.is_start():
            self.start()
        
        if not self.is_stop() and self.is_start():
            self.actions[self.current_action].run(self.robot)
            self.current_action += 1