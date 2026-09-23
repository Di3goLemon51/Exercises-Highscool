class Libro:

    # 
    def __init__(self, nome, autore, annoPubblicazione):
        self.nome = nome
        self.autore = autore
        self.annoPubblicazione = annoPubblicazione
        
    def getInfo(self):
        return f'{self.nome}, {self.autore.getInfo()}, {self.annoPubblicazione}'
        
    def getNome(self):
        return self.nome
        
    def getAutore(self):
        return self.autore.getInfo()
        
    def getAnno(self):
        return self.annoPubblicazione
    
    def setNome(self, nome):
        self.nome = nome

    def setNome(self, nome):
        self.nome = nome

    def setAnno(self, nome):
        self.nome = nome