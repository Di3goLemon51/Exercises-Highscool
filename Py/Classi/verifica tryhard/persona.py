class  Persona:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []

    def getNome(self):
        return self.nome
    
    def getMatricola(self):
        return self.matricola
    
    def getCorso(self, matricola):
        for corso in self.corsi:
            if matricola == corso.getMatricola():
                return f"{corso.getNome()}  {corso.getMatricola()} {corso.getDurata()}"
            
        raise('Corso non trovato')
    
    def getListaCorsi(self):
        for corso in self.corsi:
            print(f'{corso.getNome()}  {corso.getMatricola()} {corso.getDurata()}')

    def setNome(self, nome):
        self.nome = nome

    def setMatricola(self, matricola):
        self.matricola = matricola

    def addCorso(self, corso):
        self.corsi.append(corso)