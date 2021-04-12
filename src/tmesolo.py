
def dessine( robot):
    while True:
        if robot.crayon:
            robot.down()
        else:
            robot.up()
        sleep(1)


def q12(): 
    from threading import Thread
    from controller.strategies import Tourner
    from utils.config import Config
    from controller.controleur import Controleur
    from controller.strategies import Avancer

    controleur = Controleur()

    # protection du config
    config = Config()

    if (config.get_vers() != 0.4):
        print("Config version non conforme")
        print(config.get_vers())
        exit(1)

    if (config.get_dist_secu() < 13.0):
        print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
        exit(1)

    mode = config.get_mode()

    FPS = config.get_fps()

    if (mode):  # Mode Simu
        print("Simu on")

        from view.affichage import Affichage
        from model.robot import Robot
        from model.arene import Arene
        from utils.tools import Point
        from model.obstacles import Obstacle
        import sys

        arene = Arene()
        robot = Robot(Point(230, 300), arene)
        arene.set_robot(robot)

        affichage = Affichage(arene)

        strat = Avancer( robot , 500 , 150 )

        controleur.add_startegie(strat)
        controleur.select_startegie(0)

        thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
        thread_modele = Thread(target=arene.boucle, args=(FPS,))
        thread_affichage = Thread(target=affichage.boucle, args=(FPS,))
        thread_dessin = Thread(target=dessine, args=(arene.robot, ))

        thread_controleur.start()
        thread_modele.start()
        thread_affichage.start()
        thread_dessin.start()



def q21() :
    from threading import Thread
    from controller.strategies import Tourner
    from utils.config import Config
    from controller.controleur import Controleur
    from controller.strategies import Triangle

    controleur = Controleur()

    # protection du config
    config = Config()

    if (config.get_vers() != 0.4):
        print("Config version non conforme")
        print(config.get_vers())
        exit(1)

    if (config.get_dist_secu() < 13.0):
        print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
        exit(1)

    mode = config.get_mode()

    FPS = config.get_fps()

    if (mode):  # Mode Simu
        print("Simu on")

        from view.affichage import Affichage
        from model.robot import Robot
        from model.arene import Arene
        from utils.tools import Point
        from model.obstacles import Obstacle
        import sys

        arene = Arene()

        robot = Robot(Point(230, 300), arene)
        arene.set_robot(robot)

        
        affichage = Affichage(arene)

        strat = Triangle(robot, 100, 300, 1)

        controleur.add_startegie(strat)
        controleur.select_startegie(0)

        thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
        thread_modele = Thread(target=arene.boucle, args=(FPS,))
        thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

        thread_controleur.start()
        thread_modele.start()
        thread_affichage.start()

def q22() :
    from threading import Thread
    from controller.strategies import Tourner
    from utils.config import Config
    from controller.controleur import Controleur
    from controller.strategies import Polygone

    controleur = Controleur()

    # protection du config
    config = Config()

    if (config.get_vers() != 0.4):
        print("Config version non conforme")
        print(config.get_vers())
        exit(1)

    if (config.get_dist_secu() < 13.0):
        print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
        exit(1)

    mode = config.get_mode()

    FPS = config.get_fps()

    if (mode):  # Mode Simu
        print("Simu on")

        from view.affichage import Affichage
        from model.robot import Robot
        from model.arene import Arene
        from utils.tools import Point
        from model.obstacles import Obstacle
        import sys

        arene = Arene()

        robot = Robot(Point(230, 300), arene)
        arene.set_robot(robot)

        
        affichage = Affichage(arene)

        strat = Polygone(robot, 8, 50, 150, 0)

        controleur.add_startegie(strat)
        controleur.select_startegie(0)

        thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
        thread_modele = Thread(target=arene.boucle, args=(FPS,))
        thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

        thread_controleur.start()
        thread_modele.start()
        thread_affichage.start()



def q23() :

    from threading import Thread
    from controller.strategies import Tourner
    from utils.config import Config
    from controller.controleur import Controleur
    from controller.strategies import Avancer , EviterObstacle
    import random
    from utils.tools import Point, Vecteur

    controleur = Controleur()

    # protection du config
    config = Config()

    if (config.get_vers() != 0.4):
        print("Config version non conforme")
        print(config.get_vers())
        exit(1)

    if (config.get_dist_secu() < 13.0):
        print("Erreur critique: la distance de sécurité est trop faible! (minimum 13.0)")
        exit(1)

    mode = config.get_mode()

    FPS = config.get_fps()

    if (mode):  # Mode Simu
        print("Simu on")

        from view.affichage import Affichage
        from model.robot import Robot
        from model.arene import Arene
        from utils.tools import Point
        from model.obstacles import Obstacle
        import sys

        arene = Arene()

        robot = Robot(Point( random.randint(100, 900) , random.randint(50, 850) ), arene)

        angle = random.randint(0, 360)
        robot.vec_deplacement = Vecteur.get_vect_from_angle(angle)
        robot.refresh()


        arene.set_robot(robot)

        #murs
        arene.add_obstacle(Obstacle(Point(0, 0), Point(1090 ,0)))
        arene.add_obstacle(Obstacle(Point(0, 0), Point(0 ,920)))
        arene.add_obstacle(Obstacle(Point(1090, 920), Point(1090 ,0)))
        arene.add_obstacle(Obstacle(Point(0, 920), Point(1090 ,920)))


        
        affichage = Affichage(arene)

        strat = EviterObstacle(robot, 300, float("inf"), 90, 50)


        controleur.add_startegie(strat)
        controleur.select_startegie(0)

        thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
        thread_modele = Thread(target=arene.boucle, args=(FPS,))
        thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

        thread_controleur.start()
        thread_modele.start()
        thread_affichage.start()

















    
q12()
#q21()
#q22()
#q23()
