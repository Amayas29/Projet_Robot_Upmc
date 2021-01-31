#from abc import ABC

class Objet:

    def __init__(self):
        self.isFix = false
        self.isbalise = false


    def __str__(self):
        # Juste si on a pas d'objet specifique et qu'on utilise directement le objet on aura des O
        # A voir si on le supprime ou pas ?
        return "O"