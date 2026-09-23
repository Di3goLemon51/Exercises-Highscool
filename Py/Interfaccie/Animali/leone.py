from animale import Animale

class Leone(Animale):

    # Builder
    def __init__(self, nome, età, peso) -> None:
        super().__init__(nome, età)
        self.peso = peso

    # Utility
    def info(self):
        return self.peso
    
    def parla(self):
        return 'ruggisce'

    def muove(self):
        return 'va come un fulmine'

    def mangia(self):
        return 'divora'

    def beve(self):
        return 'ingurgita'

    def dorme(self, n):
        return super().dorme(n)
    
    # Getters / Setters
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso= peso