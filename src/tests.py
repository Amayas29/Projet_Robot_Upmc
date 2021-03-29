"""
print("Choisir Strategie : ")
choix = input("1 : Avancer, 2 : Tourner, 3 : Carre")

if choix==1 :
  from test.modele.test_strategie_avancer import test
elif choix==2 :
  from test.modele.test_strategie_tourner import test
else : 
  from test.modele.test_strategie_carre import test
"""

from test.modele.test_strategie_avancer import test
test()
