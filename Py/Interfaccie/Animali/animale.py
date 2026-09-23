from abc import abstractmethod
from time import sleep

class Animale:

    # Builder
    def __init__(self, nome, età) -> None:
        self.nome = nome
        self.età = età

    # Utility
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def parla(self):
        pass

    @abstractmethod
    def muove(self):
        pass

    @abstractmethod
    def mangia(self):
        pass

    @abstractmethod
    def beve(self):
        pass

    def dorme(self, n):
        sleep(n)
        return 'ha dormito'

    # Getters / Setters
    def getNome (self):
        return self.nome
    
    def getEtà (self):
        return self.età
    
    def setNome (self, nome):
        self.nome = nome

    def setEtà (self, età):
        self.età = età