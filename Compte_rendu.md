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