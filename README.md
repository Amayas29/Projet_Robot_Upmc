# CesBGoss
#CARAUX Theophane 28602627

TME SOLO :
Dans src/tmesolo.py

q1.1 :
Les modifs sont dans robot.py : j'ai rajouter un boolean crayon qui permet de savoir si il faut dessiner ou non ainsi que les fonctions up() et down() qui changent la valeur de crayon
Affichage.py : rajout d'une boucle pour afficher les pointillés si crayon=True ( petit prb : pygame efface ensuite les traits avec display, pas le temps de régler le prb)

q1.2 :
J'utilise donc mon arene et mon robot avec une stratégie Avancer et une fonction "dessine" qui permet d'alterné les up et down

q2.1 : j'ai importé dans la fonction tout ce dont j'avais besoin pour faire mon triangle
controller/strategies.py contient les stratégies, j'ai donc créer la stratégie Triangle ( on répète 3 fois les memes actions Avancer+Tourner, donc 6 actions)

q2.2 : 
J'ai repris la meme stratégie qu'un carré ou qu'un triangle
Cependant la formule donné dans l'exercice ne correspond pas à nos degrés attendues, j'ai donc remplacé la rotation pa 360/n degré et ça fonctionne, j'ai finalement ré utiliser la formule donné, cela revient au meme que 360/n)

q2.3 :
J'ai placé dans le main les murs sur les 4 limites du terrain et j'utilise une stratégie qu'on avait déjà implémenter pour avancer jusqu'a un obstacle ( marche pas )

