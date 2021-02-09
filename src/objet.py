
# Classe qui représente un objet
class Objet:

    # Constructeur
    def __init__(self):
        # initiallise les attributs qui permettent quel type d'objet il représente
        self.is_fix = False
        self.is_balise = False


    def __str__(self):
        # Juste si on a pas d'objet specifique et qu'on utilise directement le objet on aura des O
        # A voir si on le supprime ou pas ?
        return "O"


# Qui represente les cases non definie dans la vision
class NotDefined(Objet):

    def __str__(self):
        return "ND"