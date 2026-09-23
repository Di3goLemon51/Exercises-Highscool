class Persona:

    # Costruttore
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
    
    # Getters
    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getMatricola(self):
        return self.matricola
    
    # Setters
    def setNome(self, nome):
        self.nome = nome

    def setCognome(self, cognome):
        self.cognome = cognome

    def setMatricola(self, matricola):
        self.matricola = matricola