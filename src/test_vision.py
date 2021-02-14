from vision import Vision 

if __name__ == "__main__" :
    v = Vision( 20 , 30 )
    try :
        assert( v.larg == 20)
        assert( v.long == 30)
        assert( v.elements != [1,2,3,4])

        assert( v.libre_sur( 10 , 3 , 20 , 2 , 2) == True )


    except :
        print("le test à échoué !")