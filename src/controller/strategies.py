from abc import abstractmethod
from math import pi
import cv2
from PIL import Image

class Strategie(object):
    """
        Une classe abstraite qui represent toute startegie du robot

        Elle contient des methode start pour la lancer et stop pour l'arreter

        Ainsi qu'une méthode run qui est appeler en mode asynchrone à chaque mise à jour du controleur
    """

    def __init__(self, wrapper):
        # Le wrapper
        self.wrapper = wrapper

        # Les variables pour gerer l'execution et l'arret
        self.is_stop = False
        self.is_start = False

    def start(self):
        """
        voir -> None
        Lance la startegie en changeant ses booleans
        """
        self.is_stop = False
        self.is_start = True

    def stop(self):
        """
        None -> None
        Arrete la startegie
        """
        self.wrapper.stop()
        self.is_stop = True

    @abstractmethod
    def run(self):
        """
        Methode abstraite qui execute à chaque pas de temps la startegie
        """
        pass


class Avancer(Strategie):
    """
        La premiere startegie elementaire pour le mouvement : Avancer le robot de x mm à une vitesse de y
    """

    def __init__(self, wrapper, distance, vitesse):

        super().__init__(wrapper)

        # Initialse les attributs
        self.distance = distance
        self.distance_parcouru = 0  # Pour garder la distance parcourue
        self.vitesse = vitesse

    def start(self):
        """
        Overide
        """
        super().start()
        self.wrapper.stop()
        # Enregistre les donnes intitaile du robot pour calculer la distance à chaque pas de temps
        self.wrapper.begin(self, 0)
        # Remet droit le servo du robot
        self.wrapper.tourner_servo(90)
        self.distance_parcouru = 0

    def run(self):
        """
        Overide
        """

        # Si la startegie est arretee on fait rien
        if self.is_stop:
            return

        # Si il n'est pas encore lancee on la lance
        if not self.is_start:
            self.start()

        # On remet droit le servo du robot
        self.wrapper.tourner_servo(90)

        # On ajoute la distance parcourue
        self.distance_parcouru += self.wrapper.get_distance_parcouru(self, 0)

        # On test si on a atteint la distance voulue : si c'est le cas on arrete la startegie
        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de avancer __dist__ :", self.distance_parcouru,
                  self.wrapper.get_distance())
            return

        # Sinon on fait avancer le robot
        self.wrapper.avancer(self.vitesse)


class Tourner(Strategie):
    """
        La deuxieme startegie elementaire pour le mouvement : Tourner le robot de x degrees dans une direction à une vitesse de y
    """

    # Code des orientations
    GAUCHE = 1
    DROITE = 0

    def __init__(self, wrapper, angle, orientation, vitesse, servo_fix=False):
        super().__init__(wrapper)

        # On initialise tout les champs
        if orientation != self.DROITE and orientation != self.GAUCHE:
            orientation = self.GAUCHE

        self.orientation = orientation
        self.vitesse = vitesse

        # On calcule la distance à parcourir pour tourner de x degrees
        self.distance = (wrapper.WHEEL_BASE_CIRCUMFERENCE * angle) / 180

        self.distance_parcouru = 0

        # Un boolean pour savoir si on fixe le servo ou pas
        self.servo_fix = servo_fix

    def start(self):
        """
        Overide
        """
        super().start()
        # Enregistre les donnes intitaile du robot pour calculer la distance à chaque pas de temps
        self.wrapper.begin(self, self.orientation)
        self.distance_parcouru = 0

    def run(self):
        """
        Overide
        """

        # Si la startegie est arretee on fait rien
        if self.is_stop:
            return

        # Si la startegie n'est pas lancee, on la lance
        if not self.is_start:
            self.start()

        # Si le servo n'est pas fixé : on le tourne à la mêmes direction où on tourne pour verifier si on a des collisions ou pas
        if not self.servo_fix:

            if self.orientation == self.GAUCHE:
                self.wrapper.tourner_servo(110)
            else:
                self.wrapper.tourner_servo(60)

        # On mets à jour la distance parcourue
        self.distance_parcouru += self.wrapper.get_distance_parcouru(
            self, self.orientation)

        # Si on a atteint la distance à parcourir on arrete la startegie
        if self.distance_parcouru >= self.distance:
            self.stop()
            print("Arret de tourner __dist__ :", self.distance_parcouru,
                  self.wrapper.get_distance())
            return

        # On réduit la vitesse si il nous reste que quelques degrees pour ne pas dépasser
        vitesse = self.vitesse
        print(self.distance-self.distance_parcouru)
        #if self.distance_parcouru > self.distance / 2:
         #   vitesse /= 2

        #if self.distance_parcouru > self.distance * 3/4:
         #   vitesse /= 3
        
        if self.distance - self.distance_parcouru <=50 :
            self.distance_parcouru = self.distance+1
            print("return",self.distance-self.distance_parcouru )
            self.stop()
            return
        
        # On lance la méthode tourner du robot
        self.wrapper.tourner(self.orientation, vitesse)


class Switcher(Strategie):
    """
        C'est une méta-startegie qui permet d'alterner entre deux startegie avec une condtition spécifique
    """

    def __init__(self, strat_1, strat_2, fct_switcher):
        super().__init__(strat_1.wrapper)

        # On enregistre les deux startegie, ainsi que la fonction qui determine la startegie à lancer
        self.strat_1 = strat_1
        self.strat_2 = strat_2

        # Pour garder la startegie courrante
        self.current = strat_1

        self.fct_switcher = fct_switcher

    def stop(self):
        """
        Overide
        """
        super().stop()

        # On arrete les deux strategies
        self.strat_1.stop()
        self.strat_2.stop()

    def run(self):
        """
        Overide
        """

        # Si la startegie est arrete
        if self.is_stop:
            return

        # Si elle n'est pas lancee, on la lance
        if not self.is_start:
            self.start()

        if self.strat_1.is_stop and self.strat_2.is_stop:
            self.stop()
            return

        # On determine la startegie courrante
        self.current = self.fct_switcher(
            self.current, self.strat_1, self.strat_2)

        # On lance la startegie selectionnee
        self.current.run()


class SwitcherSequentiel(Switcher):
    """
        Une méta-startegie qui hérite de Switcher, c'est une startegie qui alterne entre deux strategie aussi
        mais avec une fonction de condtition déja codé qui execute la séquence (s1, s2) : 2 * max_number
    """

    def __init__(self, strat_1, strat_2, max_number):
        super().__init__(strat_1, strat_2, SwitcherSequentiel.fct_switcher)
        # On initialise les champs
        self.number = 0
        self.max_number = max_number
        self.current = self.strat_1

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        # Si on a fait nb itération de la séquence on arrete la startegie
        if self.number == self.max_number:
            self.stop()
            return

        # Sinon on determine la startegie à executer
        curr = self.fct_switcher(
            self.current, self.strat_1, self.strat_2)

        # Si c'est pas la même qu'avant donc on a fait une itération dans la séquence
        if curr != self.current:
            self.current = curr
            self.number += 1

        self.current.run()

    @staticmethod
    def fct_switcher(current, strat_1, strat_2):
        """
        Startegie * Startegie * Startegie -> Startegie

        Elle sélectionne la startegie à executer
        """

        # Si la startegie courrante est s1
        if current == strat_1:

            # Si s1 s'est terminee on lance s2 et on la retourne
            if strat_1.is_stop:
                strat_2.start()
                return strat_2

            # Sinon on continue l'execution de s1
            return strat_1

        # De maniere symetrique pour s2
        if strat_2.is_stop:
            strat_1.start()
            return strat_1
        return strat_2


class Unitaire(Strategie):
    """
        Une méta-startegie qui permet d'envelopper une startegie avec une condtition d'arret du robot
    """

    def __init__(self, strat, fct_arret):
        super().__init__(strat.wrapper)
        self.strat = strat
        self.fct_arret = fct_arret

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.strat.stop()

    def run(self):
        """
        Overide
        """

        # Si la condtition d'arret est verifiee, on arrete le robot
        if self.fct_arret():
            self.wrapper.stop()
            return

        if self.strat.is_stop:
            self.stop()
            return

        # Sinon on lance la startegie
        self.strat.run()


class AvancerAuMur(Strategie):
    """
        Strategie qui permet au robot qu'il avance avec une vitesse donnée tout droite et qu'il s'arrete avant avec une distance de sécurite donnée
    """

    def __init__(self, wrapper, vitesse, securite):
        super().__init__(wrapper)

        self.securite = securite

        # la startegie avancer avec une vitesse d'une distance infinie
        avancer = Avancer(wrapper, float("inf"), vitesse)

        # Envelopper la startegie avec la condition d'arret (le get_distance <= securite)
        self.strat = Unitaire(avancer, self.fct_arret)

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        """
        Overide
        """
        super().start()
        self.strat.start()

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.strat.stop()

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.strat.is_stop:
            self.stop()
            return

        self.strat.run()


class Carre(Strategie):
    """
        Strategie qui permet au robot de dessiner un carre de cote donné avec une vitesse donné le tout en respectant une distance de sécurite pour les collisions
    """

    NB_MAX = 8

    def __init__(self, wrapper, cote, vitesse, orientation, securite):
        super().__init__(wrapper)

        # On creér la startegie qui va dessiner les coté
        avancer = Avancer(wrapper, cote, vitesse)

        # La startegie de tourner de 90 degrees
        tourner = Tourner(wrapper, 90, orientation, vitesse)

        # Ensuite on alterne entre les deux strategies 8 fois
        switcher = SwitcherSequentiel(avancer, tourner, self.NB_MAX)

        # Et on enveloppe le tout avec la condtition de securite
        self.switcher = Unitaire(switcher, self.fct_arret)

        self.securite = securite

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        """
        Overide
        """
        super().start()
        self.switcher.start()

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.switcher.stop()

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.switcher.is_stop:
            self.stop()
            return

        self.switcher.run()


class Triangle(Strategie):

    """
        Strategie pour dessiner un triangle équilatéral de coté donnée
    """

    NB_MAX = 6

    def __init__(self, wrapper, cote, vitesse, orientation, securite):
        super().__init__(wrapper)

        # Pour dessiner les coté
        avancer = Avancer(wrapper, cote, vitesse)

        # Pour les angles
        tourner = Tourner(wrapper, 120, orientation, vitesse)

        # On alterne entre les deux startegies 6 fois
        switcher = SwitcherSequentiel(avancer, tourner, self.NB_MAX)

        # Pour la securite
        self.switcher = Unitaire(switcher, self.fct_arret)
        self.securite = securite

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        """
        Overide
        """
        super().start()
        self.switcher.start()

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.switcher.stop()

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.switcher.is_stop:
            self.stop()
            return

        self.switcher.run()


class EviterObstacle(Strategie):

    """
        Startegie qui permet d'avancer d'une distance donnée tout en evitant les obstacles
    """

    def __init__(self, wrapper, vitesse, distance, angle, securite):
        super().__init__(wrapper)

        # La startegie pour avancer
        avancer = Avancer(wrapper, distance, vitesse)

        # La startegie de tourner pour éviter les collisions
        tourner = Tourner(wrapper, angle, Tourner.DROITE, vitesse)

        # Pour alterne entre les deux startegies avec une condtition
        switcher = Switcher(avancer, tourner, self.fct_switcher)

        # Pour la distance de securite
        self.switcher = Unitaire(switcher, self.fct_arret)
        self.securite = securite

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        """
        Overide
        """
        super().start()
        self.switcher.start()

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.switcher.stop()

    def fct_switcher(self, current, avancer, tourner):

        wrapper = avancer.wrapper

        # Si on est proche d'un obstacle
        if wrapper.get_distance() <= self.securite:

            # On prépare la méthode tourner
            tourner.start()

            # On tourner le servo à droite
            wrapper.tourner_servo(60)

            # Si on a un obstacle à droite on change la direction à gauche
            if wrapper.get_distance() <= self.securite:
                tourner.orientation = Tourner.GAUCHE

            return tourner

        return avancer

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.switcher.is_stop:
            self.stop()
            return

        self.switcher.run()

        # On remet l'orientation de la startegie tourner à droite
        self.switcher.strat.strat_2.orientation = Tourner.DROITE


class SuivreBalise(Strategie):
    """
        La startegie de suivi d'une balise
    """

    def __init__(self, wrapper, vitesse, image_loader=None):
        super().__init__(wrapper)

        # La startegie de tourner, elle sera mise à jour à chaque fois dans le run
        self.tourner = Tourner(wrapper, 0, 0, vitesse, True)

        # La startegie avancer qui avancer d'une vitesse à une distance infinie
        self.avancer = Avancer(wrapper, float("inf"), vitesse)

        # On alterne entre les deux startegies en suivant une fonction de selection
        switcher = Switcher(self.avancer, self.tourner, self.fct_switcher)

        # La securite pour les collisions
        self.switcher = Unitaire(switcher, self.fct_arret)

        # Permet de reccuperer l'image du robot de façon asynchrone (si mode irl)
        self.image_loader = image_loader

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= 50

    def fct_switcher(self, current, avancer, tourner):
        """
        Startegie * Startegie * Startegie -> Startegie

        Permet de selectionner la startegie à executer en cherchant la balise dans l'image capturé si mode irl sinon dans la vision du robot
        """

        # On remet droit le servo du robot
        self.wrapper.tourner_servo(90)

        # On calcule l'angle et l'orientation de la balise par apport au robot
        angle, orientation = self.wrapper.get_angle_orientation_balise(
            self.image_loader)

        # Si l'angle est -1 donc on a pas trouvé donc on lancer une rotation sur 360 pour la chercher
        if angle == -1:
            angle = 360
            orientation = self.wrapper.DROITE
            self.wrapper.tourner_servo(90)

        # Si l'angle est <= 30 donc on a trouve la balise on avancer directement vers elle
        if angle <= 30:
            return avancer

        # Sinon si l'angle est != -1 et > 30 on tourner de l'angle pour se remettre droite face à la balise
        tourner.orientation = orientation

        tourner.distance = (
            self.wrapper.WHEEL_BASE_CIRCUMFERENCE * angle) / 180

        tourner.start()

        return tourner

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.switcher.is_stop:
            self.stop()
            return

        self.switcher.run()


class PolygoneRegulier(Strategie):
    """
        Startegie qui permet de dessiner un polygone regulier de nombre coté
    """

    def __init__(self, wrapper, nombre, cote, vitesse, orientation, securite):

        if nombre <= 0:
            print("Le nombre doit etre > 0")
            return

        super().__init__(wrapper)

        self.securite = securite

        # Pour dessiner les coté
        avancer = Avancer(wrapper, cote, vitesse)

        # Calcule de l'angle entre chaque coté
        angle = 180 - (180 * (((nombre - 2) * pi) / nombre)) / pi

        # La startegie de tourner pour les angle
        tourner = Tourner(wrapper, angle, orientation, vitesse)

        # Alterner les startegies 2 * nombre fois
        switcher = SwitcherSequentiel(avancer, tourner, 2 * nombre)

        # La securite pour les obstacles
        self.switcher = Unitaire(switcher, self.fct_arret)

    def fct_arret(self):
        """
        None -> None
        Condition d'arret : get_distance <= securite
        """
        return self.wrapper.get_distance() <= self.securite

    def start(self):
        """
        Overide
        """
        super().start()
        self.switcher.start()

    def stop(self):
        """
        Overide
        """
        super().stop()
        self.switcher.stop()

    def run(self):
        """
        Overide
        """

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        if self.switcher.is_stop:
            self.stop()
            return

        self.switcher.run()


def get_forme(frame):
    """
    Image -> List * int
    Permet de reccuperer les masks de l'image apres applications de la selection des couleurs ainsi que le nombre de masks non vides
    """

    # On transforme l'image en hvs
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # On boucle sur les quatre couleurs

    hsv_lower = (95, 100, 20)
    hsv_upper = (115, 255, 255)
      
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

        # On netoie un peu le mask
    mask = cv2.erode(mask, None, iterations=4)
    mask = cv2.dilate(mask, None, iterations=4)

    # On chercher toutes les formes detecter
    elements, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    n = -1
    for cnt in elements:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        n = max(n, len(approx))
        
    return n



class DessineMoi(Strategie):

    def __init__(self, wrapper):
        super().__init__(wrapper)
        self.strat = None

    def start(self):
        """
        Overide
        """
        super().start()

        if self.strat is not None:
            self.strat.start()

    def stop(self):
        """
        Overide
        """
        super().stop()

        if self.strat is not None:
            self.strat.stop()
            self.strat = None

    def run(self):

        if self.is_stop:
            return

        if not self.strat:
            self.start()

        if self.strat is not None:

            if self.strat.is_stop:
                print("fin")
                self.strat = None

            else:
                self.wrapper.allumer(self.wrapper.GREEN)
                self.strat.run()

        if self.strat is None:

            self.wrapper.allumer(self.wrapper.ORANGE)

            frame = self.wrapper.robot.get_image()
            
            if frame is None:
                self.wrapper.allumer(self.wrapper.RED)
                return
            
            img = Image.fromarray(frame)
            img.save("image.png")
            
            img = cv2.imread("image.png")
            
            nombre = get_forme(img)
            print(nombre)

            if nombre == -1:
                self.wrapper.allumer(self.wrapper.RED)
                return
            
            self.strat = PolygoneRegulier(self.wrapper, nombre, 100, 200, 1, 100)
            self.wrapper.allumer(self.wrapper.GREEN)
