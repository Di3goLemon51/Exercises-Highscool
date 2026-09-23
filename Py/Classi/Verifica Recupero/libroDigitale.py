from libro import Libro

class LibroDigitale(Libro):

    def __init__(self, nome, autore, annoPubblicazione, formato):
        super().__init__(nome, autore, annoPubblicazione)
        self.formato = formato

    def getFormato(self):
        return self.formato
    
    def getInfo(self):
        return f'{super().getInfo()}, {self.getFormato}'