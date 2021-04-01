
print("Choisir Strategie : ")
msg = "\t1- Avancer.\n\t2- Tourner.\n\t3- Carre\n"
choix = int(input(msg))

try:
    if choix == 1:
        from test.modele.test_strategie_avancer import test
    elif choix == 2:
        from test.modele.test_strategie_tourner import test
    elif choix == 3:
        from test.modele.test_strategie_carre import test
    else:
        raise ValueError("Mauvais choix")
except Exception as e:
    print("Erreur : ", e)

test()
