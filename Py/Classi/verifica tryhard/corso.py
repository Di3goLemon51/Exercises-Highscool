class Corso:
    
    def __init__(self, nome, matricola, durata):
        self.nome = nome
        self.matricola = matricola
        self.durata = durata

    def getNome(self):
        return self.nome
    
    def getMatricola(self):
        return self.matricola
    
    def getDurata(self):
        return self.durata
    
    def setNome(self, nome):
        self.nome = nome

    def setMatricola(self, matricola):
        self.matricola = matricola

    def setDurata(self, durata):
        self.durata = durata