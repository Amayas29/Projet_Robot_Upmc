# Compte rendu

## Semaine 1 

### Organisation

  - Vérifier que tout le monde a compris la POO en python
  - Etablissement des taches à faire pour la semaine
  - Changement de groupe, expliquer aux nouveaux membres le projet pour bien tous partir sur la meme idée

### Description des classes

  Création des classes et méthodes nécessaire à la réalisation de la simulation :
  - Robot.py : représente le robot
  - Simulation.py : délimiter la grille avec des murs
  - Vision.py : représente la vision du robot avec une grille
  - Objet.py / Wall.py : objets placés sur la la grille ( obstacles )
  - Echelle.py : établi le nombre de cases pour une echelle donnée
  - Classes de tests pour vérifier le bon comportement des classes 

### Conclusion

  - Fin de semaine 1 : on peut placer le robot et des objets sur le terrain, on peut afficher le terrain et la vision avec les objets
  
  
## Semaine 2

### Organisation

  - Commenter les codes pour ne pas perdre leur utilisation
  - S'occuper de la synchronisation de la vision avec la simulation
  - Changer les méthodes statiques de `Static.py` en fonction importable
  - Création du système de déplacement (Méthode DeplaceRobSim, Completion méthode deplaceRobot)

### Done

  - Changement de Static.py en Tool.py, et donc s'occuper de revoir l'utilisation de Static.py dans les classes qui l'utilisait
  - Tous les codes sont commentés
  - Création de la vision synchronisé avec la simulation pour pouvoir voir comme le robot
  - Création de la méthode déplacement pour faire bouger le robot sur la simulation sous différents angles/directions
  - Création méthode libresur qui permet de savoir si il y a des obstacles sur le chemin
  - Création de fichiers test pour vérifier la bonne fonctionnalité des nouveaux ajouts
  - Préparation d'une démo pour le client pour lui présenter notre avancement sur le projet
  
### Conclusion

  - Fin de semaine 2 : nous sommes capables d'afficher la vision du robot et donc de transmettre au robot les informations qui lui servent à se déplacer en toute sécurité, nous sommes aussi capables de déplacer le robot et de vérifier la présence d'obstacles sur son chemin 

## Semaine 3 

### Organisation 

  - Transformer la grille en liste pour avoir quelque chose de continu et améliorer notre précision
  - Passer sur une interface graphique ( pygame )
  - Se renseigner sur l'interface graphique
  - Faire les tests unitaires

### Done

  - Les tests unitaires de toutes les classes ont été fais, les méthodes fonctionnent  comme on le souhaite
  - Nous avons avancer sur le passage en liste de la grille mais il reste beaucoup à modifier encore
  - nous avons fais quelques tests sur pygame et nous avons de nombreux problèmes

### Conclusion 

  - Fin de semaine 3 : nous avons passer la vision du robot en liste et  nous avons commencer à déplacer notre robot sur l'interface, tous nos tests sont éxécuter avec succès. Nous devons continuer de travailler sur le passage en liste et l'interface
  
### Semaine 4

### Organisation

  - Continuer d'améliorer les précisions
  - Améliorer l'interface graphique
  - Refaire les tests unitaire si tout est fini
  - Se reposer un peu car vacances
  - Refléchir au passage sur pygames
  - Réfléchir pour le passage à l'IRL

### Done 

  - les améliorations du code sont terminées, il reste cependant quelques méthodes à refaire en liste
  - le passage en liste a avancé mais il reste encore beaucoup de choses à faire


### Conclusion 

  - Fin semaine 4 : Toujours en avancement sur le passage en liste


### Semaine 5 

### Organisation

  - Finir d'utiliser les listes
  - Régler les problèmes de code etc
  
### Conclusion 
  
  - Fin semaine 5 : Nous allons refactoriser le code et tout recommencer de 0


### Semaine 6

### Organisation

  - Nous allons refactoriser le code et repartir de 0
  - Factoriser le code ( dossiers Gui/Modele/Utils/.. )
  - Refaire les classes et les méthodes
  - On utilise les istes plutot qu'une grille pour plus de précision
  - Préparer une démo théorique pygame de ce que serait notre affichage

### Done
 
  - La refactorisation du code a bien avancé
  - La démo théorique est prete
  - Beaucoup de code a été refait

### Conclusion

  - Fin semaine 6 : nous sommes donc entrain de refactoriser tout notre code, nous sommes bien reparti, l'affichage théorique est pret, beaucoup de méthodes et classes sont finies


### Semaine 7 

### Organisation

  - Finir la refactorisation
  - Travailler sur les méthodes du modele pour les déplacements
  - Faire l'affichage pygame

### Done

  - Beaucoup de méthodes complètes 
  - L'affichage est terminé
  
  
### Conclusion

  - Fin semaine 7 : La refactorisation de tout le code est finit, presque terminé la simuation, l'affichage est pret
