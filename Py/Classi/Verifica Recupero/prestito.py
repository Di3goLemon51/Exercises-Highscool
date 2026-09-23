class Prestito:

    def __init__(self, libro, utente, dataPrestito, giorniPrestito) -> None:
        self.libro = libro
        self.utente = utente
        self.dataPrestito = dataPrestito
        self.giorniPrestito = giorniPrestito

    def getLibro(self):
        return self.libro
    
    def getUtente(self):
        return self.utente
    
    def getDataPrestito(self):
        return self.dataPrestito
    
    def getGiorniPrestito(self):
        return self.giorniPrestito

    def getInfo(self):
        return f'{self.libro.getInfo()}, {self.utente.getInfo()}, {self.dataPrestito}, {self.giorniPrestito}'