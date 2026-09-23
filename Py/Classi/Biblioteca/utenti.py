from biblioteca import Biblioteca

class Utente(Biblioteca):

    # Costruttore
    def __init__(self, titolo, autore, anno, disponibilità, nome, libri):
        super().__init__(titolo, autore, anno, disponibilità)
        self.nome = nome
        self.libri = []

    # Utility
    

    # Getters


    # Setters