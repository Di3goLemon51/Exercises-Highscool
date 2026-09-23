from veicolo import Veicolo

class AutoElettrica(Veicolo):

    # Costruttore
    def __init__(self, marca, modello, potenzaWatt):
        super().__init__(marca, modello)
        self.potenzaWatt = potenzaWatt

    # Utility
    def stampaAutonomia(self) -> str:
        return f'Autonomia della {self.marca} {self.modello}: {self.potenzaWatt}'
    
    # Getters
    def getPotenzaWatt(self):
        return self.potenzaWatt