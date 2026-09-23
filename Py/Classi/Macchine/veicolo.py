class Veicolo:
    # Costruttore
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    # Utility
    def descrizione(self):
        des = self.marca + ' ' + self.modello
        return des
    
    # Getters
    def getMarca(self):
        return self.marca
    
    def getModello(self):
        return self.modello


    #Setters
    def setMarca(self, marca):
        self.marca = marca

    def setModello(self, modello):
        self.modello = modello