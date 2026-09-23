class Corso:

    # Costruttore
    def __init__(self, nomeCorso, matricola, durata):
        self.nomeCorso = nomeCorso
        self.matricola = matricola
        self.durata = durata

    # Getters
    def getNomeCorso(self):
        return self.nomeCorso
    
    def getMatricola(self):
        return self.matricola
    
    def getDurata(self):
        return self.durata
    
    # Setters
    def setNomeCorso(self, nomeCorso):
        self.nomeCorso = nomeCorso

    def setMatricola(self, matricola):
        self.matricola = matricola

    def setDurata(self, durata):
        self.durata = durata