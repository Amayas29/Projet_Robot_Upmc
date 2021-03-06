from echelle import Echelle

if __name__ == "__main__" :
    e = Echelle( 5 )
    try : 
        assert ( e.nb_cases == 5 )
    except :
        print( "le test à échoué !")