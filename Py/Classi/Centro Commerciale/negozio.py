from prodotto import Prodotto

class Negozio:

    # Builder
    def __init__(self, nome, id, tipo) -> None:
        self.nome = nome
        self.id = id
        self.tipo = tipo
        self.listaProd = []

    # Utility
    def addProd(self, nome, id, prezzo):
        prodotto = Prodotto(nome, id, prezzo)
        self.listaProd.append(prodotto)

    def getListaProd(self):
        for prodotto in self.listaProd:
            print(prodotto)

    # Getters
    def getNome(self):
        return self.nome
    
    def getId(self):
        return self.id
    
    def getTipo(self):
        return self.tipo

    def getProd(self, id):
        for prodotto in self.listaProd:
            if id == prodotto.getId():
                return prodotto
            
        raise('Prodotto non esistente')

    # Setters
    def setNome(self, nome):
        self.nome = nome

    def setId(self, id):
        self.id = id