from time import sleep


class Controleur(object):
    """
        La classe de controleur : Le controleur sert à gerer les strategies du robot
        * Il sert à sélectionner la startegie à executer

        La structure : 
        C'est un conteneur de strategies

        A chaque appel à sa methode run il test si la startegie courrante est non terminée si c'est le cas il la lance

    """

    def __init__(self):
        # La liste des startegies
        self.strategies = []

        # La startegie courrante
        self.current_strat = -1

    def add_startegie(self, strategie):
        """
        Startegie -> void
        Permer d'ajouter une startegie à la liste
        """
        self.strategies.append(strategie)

    def select_startegie(self, index):
        """
        int -> void
        Pemer de sélectionner une startegie à executer parmis toutes les startegies sauvegardées
        """
        if index < 0 or index > len(self.strategies):
            return

        self.strategies[self.current_strat].start()
        self.current_strat = index

    def boucle(self, fps):
        """
        float -> void
        Une boucle d'execution dans un thread pour des appels asynchrone pour la mise à jour du controleur
        """

        if self.current_strat < 0 or self.current_strat == len(self.strategies):
            return

        while not self.strategies[self.current_strat].is_stop:
            self.update()
            sleep(1./fps)

    def update(self):
        """
        void -> void
        Mets à jour le controleur en lançant la startegie courrante 
        """
        self.strategies[self.current_strat].run()

    def stop(self):
        """
        void -> void
        Permet d'arreter le controleur (la boucle du thread)
        """

        if self.current_strat < 0 or self.current_strat == len(self.strategies):
            return

        self.strategies[self.current_strat].stop()
