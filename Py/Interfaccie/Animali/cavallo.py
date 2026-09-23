from animale import Animale

class Cavallo(Animale):

    # Builder
    def __init__(self, nome, età, mantello) -> None:
        super().__init__(nome, età)
        self.mantello = mantello

    # Utility
    def info(self):
        return self.mantello
    
    def parla(self):
        return 'nitrisce'

    def muove(self):
        return 'galoppa'

    def mangia(self):
        return 'mangia'

    def beve(self):
        return 'si abbevera'

    def dorme(self, n):
        return super().dorme(n)
    
    # Getters / Setters
    def getMantello(self):
        return self.mantello
    
    def setMantello(self, mantello):
        self.mantello= mantello