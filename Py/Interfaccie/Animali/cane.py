from animale import Animale

class Cane(Animale):

    # Builder
    def __init__(self, nome, età, razza) -> None:
        super().__init__(nome, età)
        self.razza = razza

    # Utility
    def info(self):
        return self.razza
    
    def parla(self):
        return 'abbaia'

    def muove(self):
        return 'corre'

    def mangia(self):
        return 'mangia'

    def beve(self):
        return 'beve'

    def dorme(self, n):
        return super().dorme(n)
    
    # Getters / Setters
    def getRazza(self):
        return self.razza
    
    def setRazza(self, razza):
        self.razza= razza