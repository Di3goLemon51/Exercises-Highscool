# Gestione di una biblioteca
class Biblioteca:

    # Costruttore
    def __init__(self, titolo, autore, anno, disponibile):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.disponibile = disponibile

    # Utility
    def prestito(self):
        self.disponibile = False
    
    def restituisci(self):
        self.disponibile = True

    # Getters
    def getLibro(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, disponibile: {self.disponibile}"

    # Setters
    def setTitolo(self, titolo):
        self.titolo = titolo

    def setAutore(self, autore):
        self.autore = autore

    def setAnno(self, anno):
        self.anno = anno