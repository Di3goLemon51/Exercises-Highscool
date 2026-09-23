# Es 4
class Studente:
    # Costruttore
    def __init__(self, name, surname, età):
        self.name = name
        self.surname = surname
        self.età = età
        self.voti = []

    # Utilità
    def inserisciVoto(self, voto):
        self.voti.append(voto)

    # Getters
    def getName(self):
        return self.name + ' ' + self.surname
    
    def getMedia(self):
        if len(self.voti) > 0:
            return sum(self.voti) / len(self.voti)

    #Setters
    def setName(self, name):
        self.name = name


stu = Studente('Diego', 'Doria', 16)

stu.inserisciVoto(7)
stu.inserisciVoto(9)
stu.inserisciVoto(6)

print(stu.getName())
print(stu.getMedia())