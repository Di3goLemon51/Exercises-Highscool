class Autore:
    
    #Costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def getInfo(self):
        return self.nome + ' ' + self.cognome
        # return f'{self.nome} {self.cognome}'
        
    def getNome(self):
        return self.nome
        
    def getCognome(self):
        return self.cognome
        
    def setNome(self, nome):
        self.nome = nome
        
    def setCognome(self, cognome):
        self.cognome = cognome