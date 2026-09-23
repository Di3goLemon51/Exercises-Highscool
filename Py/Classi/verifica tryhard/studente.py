from persona import Persona

class Studente(Persona):

    def __init__(self, nome, matricola):
        super().__init__(nome, matricola)
        self.voti = []

    def addVoto(self, voto = int):
        self.voti.append(voto)

    def getVoti(self):
        for voto in self.voti:
            print(voto)

    def getMediaVoti(self):
        media = 0
        somma = 0
        for i in range(len(self.voti)):
            somma +=  self.voti[i]
            media = somma / (i + 1)

        return media