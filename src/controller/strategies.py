from abc import abstractmethod


class Strategie(object):

    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.is_stop = False
        self.is_start = False

    def start(self):
        self.is_stop = False
        self.is_start = True

    def stop(self):
        self.wrapper.stop()
        self.is_stop = True

    @abstractmethod
    def run(self):
        pass


class Avancer(Strategie):

    def __init__(self, wrapper, distance, vitesse):

        super().__init__(wrapper)
        self.distance = distance
        self.distance_parcouru = 0
        self.vitesse = vitesse

    def start(self):
        super().start()
        self.wrapper.stop()
        self.wrapper.begin(self, 0)
        self.wrapper.tourner_servo(90)
        self.distance_parcouru = 0

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        self.wrapper.tourner_servo(90)

        self.distance_parcouru += self.wrapper.get_distance_parcouru(self, 0)

        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de avancer __dist__ :", self.distance_parcouru,
                  self.wrapper.get_distance())
            return

        self.wrapper.avancer(self.vitesse)


class Tourner(Strategie):

    GAUCHE = 1
    DROITE = 0

    def __init__(self, wrapper, angle, orientation, vitesse):
        super().__init__(wrapper)

        if orientation != self.DROITE and orientation != self.GAUCHE:
            orientation = self.GAUCHE

        self.orientation = orientation
        self.vitesse = vitesse
        self.distance = (wrapper.WHEEL_BASE_CIRCUMFERENCE * angle) / 180
        self.distance_parcouru = 0

    def start(self):
        super().start()
        self.wrapper.begin(self, self.orientation)
        self.distance_parcouru = 0

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.orientation == self.GAUCHE:
            self.wrapper.tourner_servo(110)
        else:
            self.wrapper.tourner_servo(60)

        self.distance_parcouru += self.wrapper.get_distance_parcouru(
            self, self.orientation)

        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de tourner __dist__ :", self.distance_parcouru,
                  self.wrapper.get_distance())
            return

        vitesse = self.vitesse

        if self.distance_parcouru < self.distance / 2:
            vitesse /= 2

        elif self.distance_parcouru < self.distance * 3/4:
            vitesse /= 3

        # vitesse = 10 if vitesse < 10 else vitesse

        self.wrapper.tourner(self.orientation, vitesse)


class Switcher(Strategie):

    def __init__(self, strat_1, strat_2, fct_switcher):
        super().__init__(strat_1.wrapper)
        self.strat_1 = strat_1
        self.strat_2 = strat_2
        self.current = strat_1
        self.fct_switcher = fct_switcher

    def stop(self):
        super().stop()
        self.strat_1.stop()
        self.strat_2.stop()

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        self.current = self.fct_switcher(
            self.current, self.strat_1, self.strat_2)

        self.current.run()


class SwitcherSequentiel(Switcher):

    def __init__(self, strat_1, strat_2, max_number):
        super().__init__(strat_1, strat_2, SwitcherSequentiel.fct_switcher)
        self.number = 0
        self.max_number = max_number
        self.current = self.strat_1

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.number == self.max_number:
            self.stop()
            return

        curr = self.fct_switcher(
            self.current, self.strat_1, self.strat_2)

        if curr != self.current:
            self.current = curr
            self.number += 1

        self.current.run()

    @staticmethod
    def fct_switcher(current, strat_1, strat_2):

        if current == strat_1:
            if strat_1.is_stop:
                strat_2.start()
                return strat_2
            return strat_1

        if strat_2.is_stop:
            strat_1.start()
            return strat_1
        return strat_2


class Unitaire(Strategie):

    def __init__(self, strat, fct_arret):
        super().__init__(strat.wrapper)
        self.strat = strat
        self.fct_arret = fct_arret

    def stop(self):
        super().stop()
        self.strat.stop()

    def run(self):

        if self.fct_arret():
            self.strat.stop()
            return

        self.strat.run()


class Carre(Strategie):

    NB_MAX = 8

    def __init__(self, wrapper, cote, vitesse, orientation, securite):
        super().__init__(wrapper)
        avancer = Avancer(wrapper, cote, vitesse)
        tourner = Tourner(wrapper, 90, orientation, vitesse)
        switcher = SwitcherSequentiel(avancer, tourner, self.NB_MAX)
        self.switcher = Unitaire(switcher, self.fct_arret)
        self.securite = securite

    def fct_arret(self):
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        super().start()
        self.switcher.start()

    def stop(self):
        super().stop()
        self.switcher.stop()

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        self.switcher.run()


class Triangle(Strategie):

    NB_MAX = 6

    def __init__(self, wrapper, cote, vitesse, orientation, securite):
        super().__init__(wrapper)
        avancer = Avancer(wrapper, cote, vitesse)
        tourner = Tourner(wrapper, 120, orientation, vitesse)
        switcher = SwitcherSequentiel(avancer, tourner, self.NB_MAX)
        self.switcher = Unitaire(switcher, self.fct_arret)
        self.securite = securite

    def fct_arret(self):
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        super().start()
        self.switcher.start()

    def stop(self):
        super().stop()
        self.switcher.stop()

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        self.switcher.run()


class EviterObstacle(Strategie):

    def __init__(self, wrapper, vitesse, distance, angle, securite):
        super().__init__(wrapper)
        avancer = Avancer(wrapper, distance, vitesse)
        tourner = Tourner(wrapper, angle, Tourner.DROITE, vitesse)
        switcher = Switcher(avancer, tourner, self.fct_switcher)
        self.switcher = Unitaire(switcher, self.fct_arret)
        self.securite = securite

    def fct_arret(self):
        return self.wrapper.get_distance() <= 10

    def start(self):
        super().start()
        self.switcher.start()

    def stop(self):
        super().stop()
        self.switcher.stop()

    def fct_switcher(self, current, avancer, tourner):

        wrapper = avancer.wrapper

        if wrapper.get_distance() <= self.securite:

            tourner.start()

            wrapper.tourner_servo(60)

            if wrapper.get_distance() <= self.securite:
                tourner.orientation = Tourner.GAUCHE

            return tourner

        return avancer

    def run(self):
        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        self.switcher.run()
        self.switcher.strat.strat_2.orientation = Tourner.DROITE


