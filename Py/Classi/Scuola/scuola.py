from corso import Corso
from docente import Docente
from studente import Studente

class Scuola:

    # Costruttore
    def __init__(self, nome):
        self.nome = nome
        self.corsi = []
        self.docenti = []
        self.studenti = []

    # Utility
    def addCorso(self, nomeCorso, matricola, durata):
        corso = Corso(nomeCorso, matricola, durata)
        self.corsi.append(corso)

    def addDocente(self, nome, cognome, matricola):
        docente = Docente(nome, cognome, matricola)
        self.docenti.append(docente)

    def addStudente(self, nome, cognome, matricola):
        studente = Studente(nome, cognome, matricola)
        self.studenti.append(studente)

    # Getters
    def getNome(self):
        return self.nome
    
    # Setters
    def setNome(self, nome):
        self.nome = nome

    def getCorsi(self):
        for corso in self.corsi:
            print(f'Nome: {corso.nomeCorso}, Marticola: {corso.matricola}, Durata: {corso.durata}')
            
    def getDocenti(self):
        for docente in self.docenti:
            print(f'Nome e Cognome: {docente.nome} {docente.cognome}, Marticola: {docente.matricola}')

    def getStudenti(self):
        for studente in self.studenti:
            print(f'Nome e Cognome: {studente.nome} {studente.cognome}, Marticola: {studente.matricola}')