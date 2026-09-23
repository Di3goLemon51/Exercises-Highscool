from persona import Persona
from corso import Corso

class Docente(Persona):

    # Costruttore
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome, matricola)
        self.corsi = []

    # Utility
    def addCorso(self, nomeCorso, matricola, durata):
        corso = Corso(nomeCorso, matricola, durata)
        self.corsi.append(corso)

    # Getters
    def getCorsi(self):
        return self.corsi
    
    def getCorsi(self):
        for corso in self.corsi:
            print(f'Nome: {corso.nomeCorso}, Marticola: {corso.matricola}, Durata: {corso.durata}')