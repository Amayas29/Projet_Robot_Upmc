from robot import Robot
from tool import add_objet, affiche
from simulation import Simulation

if __name__ == "__main__" :
    r = Robot( 10 )
    
    try :

        assert( r.taille_robot == 2 )
        r.set_simu( True )
        assert( r.is_simu == True)
        assert( r.vision.libre_sur( 10 , r.taille_robot , 20 , 0 , 0) == True )
        assert( r.deplace_robot(10 , 10 , 20 ) == True )
        assert( r.deplace_robot(10 , 10 , 45 )== False)
        

    except :
        print("le test à échoué !")
