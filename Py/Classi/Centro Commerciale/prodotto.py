class Prodotto:
    
    # Builder
    def __init__(self, nome, id, prezzo) -> None:
        self.nome = nome
        self.id = id
        self.prezzo = prezzo

    # Getters
    def getNome(self):
        return self.nome
    
    def getId(self):
        return self.id
    
    def getPrezzo(self):
        return self.prezzo
    
    # Setters
    def setNome(self, nome):
        self.nome = nome

    def setId(self, id):
        self.id = id

    def setPrezzo(self, prezzo):
        self.nome = prezzo