from libro import Libro

class LibroCartaceo(Libro):

    def __init__(self, nome, autore, annoPubblicazione, numPag):
        super().__init__(nome, autore, annoPubblicazione)
        self.numPag = numPag

    def getNumPag(self):
        return self.numPag
    
    def getInfo(self):
        return f'{super().getInfo()}, {self.getNumPag}'