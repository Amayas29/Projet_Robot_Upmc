import Vision
        
def testAdd_Objet(vision):
    vision.add_Objet("test",1,1)
    assert vision.grille[1][1] == "test"
    vision.add_Objet("test2",1,1)
    assert vision.grille[1][1] == "test"
        
    for i in range(2,vision.long):
        for j in range(2,vision.larg):
                vision.add_Objet(i,i,j)
                assert vision.grille[i][j]==i


if __name__ == '__main__':
    v = Vision.Vision(10, 10)
    try:
        testAdd_Objet(v)
        print("Test: Add Objet successful")
    except AssertionError as e:
        print(e)
