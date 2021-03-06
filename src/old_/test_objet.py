from objet import Objet
from wall import Wall
from robotsimu import RobotSimu


if __name__ == "__main__" :
    o = Objet()
    w = Wall()
    r = RobotSimu()

    try :
        assert( o.is_fix == False )
        assert( o.posx == None )
        assert( o.posy == None)
        assert( w.is_fix == True )
        assert( r.direction == 0 )
        r.set_pos( 1 , 2 , 10 )
        assert( r.posx == 1 )
        assert( r.posy == 2 )
        assert( r.direction == 10 )
        r.set_pos( -1 , 2 , 10 ) 
        assert( r.posx == 1 )
        assert( r.posy == 2 )
        assert( r.direction == 10 )

      


    except :
        print("le test à échoué !")