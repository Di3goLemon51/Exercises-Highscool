from negozio import Negozio

class Centro:
    
    # Builder
    def __init__(self, nome) -> None:
        self.nome = nome
        self.listaNeg = []

    # Utility
    def addNeg(self, negozio):
        self.listaNeg.append(negozio)

    def getListaNeg(self):
        for negozio in self.listaNeg:
            print(negozio)

    # Getters
    def getNome(self):
        return self.nome
    
    def getNeg(self, id):
        for negozio in self.listaNeg:
            if id == negozio.getId():
                return negozio
            
        raise('Negozio non esistente')

    # Setters
    def setNome(self, nome):
        self.nome = nome