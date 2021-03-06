from simulation import Simulation
from vision import Vision
from echelle import Echelle
from tool import add_objet, is_occupe, __distance_points__ , normalise_angle, __get_milieu__ , distance , angle , norme , produit_scalaire, to_degree , to_radian




if __name__ == "__main__" :
    v = Vision( 20 , 20 )
    e= Echelle( 2 )
    s = Simulation( 20 , 30 , e , v , 4 )
    try : 
        assert( s.larg == 20*2 )
        assert( s.long == 30*2 )
        assert( len(s.grille) == s.larg )

        for i in range( 0 , s.larg ):
            assert( len(s.grille[i]) == s.long )
        

        assert( is_occupe( s.grille , 0 , 0) == True )
        assert( add_objet(s.grille , "O" , 0 , 0 ) == False )
        

        assert( to_degree(2.0) == 114.59155902616465 )
        assert( to_radian( 90 ) == 1.5707963267948966 )

        assert( produit_scalaire( (1,1) , (2,2) ) == 4 )
        assert( norme( (5,7) ) == 8.602325267042627 )
        assert( angle ( (1,3) , (5,4) ) == 32.91 )
        assert( __distance_points__( [1,1] , [2,2]) == 1.4142135623730951 )
        assert( normalise_angle( 370 ) == 10 )
        assert( normalise_angle( 370 ) != 370 )
        assert( __get_milieu__( [1,1] , [3,3]) == (2,2))
        assert( distance( [0,1,2] , [5,5]) == 7.0 )


        assert( is_occupe( s.grille , s.robot_simu.posx ,s.robot_simu.posy ) == True )

        for j in range(len(s.grille)) :
            assert( is_occupe( s.grille , j , 0 ) == True)
            assert( is_occupe( s.grille , j , len(s.grille[0])-1 ) == True )
        for jj in range(len(s.grille[0])) :
            assert( is_occupe( s.grille , 0 , jj) == True )
            assert( is_occupe( s.grille , len(s.grille)-1 , jj) == True )

        x = s.robot_simu.posx
        y = s.robot_simu.posy 
        s.__enlever_robot_map__() 
        assert( is_occupe( s.grille , x , y) == False )

        s.__placer_robot__( 5 , 5 , 45)
        assert( is_occupe( s.grille , 5 , 5) == True )


    except :
        print("le test à échoué !")