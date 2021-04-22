from time import sleep


class Controleur(object):

    def __init__(self):
        self.strategies = []
        self.current_strat = -1

    def add_startegie(self, strategie):
        self.strategies.append(strategie)

    def select_startegie(self, index):
        if index < 0 or index > len(self.strategies):
            return

        self.strategies[self.current_strat].start()
        self.current_strat = index

    def boucle(self, fps):

        if self.current_strat < 0 or self.current_strat == len(self.strategies):
            return

        while not self.strategies[self.current_strat].is_stop:
            self.update()
            sleep(1./fps)

    def update(self):
        self.strategies[self.current_strat].run()

    def stop(self):

        if self.current_strat < 0 or self.current_strat == len(self.strategies):
            return

        self.strategies[self.current_strat].stop()
