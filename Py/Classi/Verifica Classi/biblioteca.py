class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.listaLibri = []
        
    def addLibro(self, libro):
        self.listaLibri.append(libro)
        
    def getListaLibri(self):
        lista = []
        for libro in self.listaLibri:
            lista.append(libro.getInfo())
            
        return lista
            
    def getListaAutore(self, autore):
        lista = []
        for libro in self.listaLibri:
            if autore.getInfo() == libro.getAutore():
                lista.append(libro.getInfo())
                
        return lista
    
    def getNome(self):
        return self.nome
        
    def setNome(self, nome):
        self.nome = nome