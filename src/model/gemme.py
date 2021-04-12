class Gemme():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.en_vie = True
    
    def mourir(self):
        self.en_vie = False