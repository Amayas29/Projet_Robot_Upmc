
# Classe qui représente un objet
class Objet:

    # Constructeur
    def __init__(self):
        # initiallise les attributs qui permettent quel type d'objet il représente
        self.isFix = False
        self.isbalise = False


    def __str__(self):
        # Juste si on a pas d'objet specifique et qu'on utilise directement le objet on aura des O
        # A voir si on le supprime ou pas ?
        return "O"
