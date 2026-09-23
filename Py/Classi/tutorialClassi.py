class Persona:
    # Costruttore
    def __init__(self, name, surname):
        self.nome = name
        self.cognome = surname
        self.voti = []

    # Utilità
    def inserisciVoto(self, voto):
        self.voti.append(voto)

    # Getters
    def getName(self):
        return self.name
    
    def getMedia(self):
        if len(self.voti) > 0:
            return sum(self.voti) / len(self.voti)

    #Setters
    def setName(self, name):
        self.name = name

# ------------------------------------------------

studente = Persona('Diego', 'Doria')
print(studente.getName())

studente.setName('NicoBag')
print(studente.getName())