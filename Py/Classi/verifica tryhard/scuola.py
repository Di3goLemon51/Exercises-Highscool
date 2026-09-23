class Scuola:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []
        self.studenti = []
        self.docenti = []

    def getNome(self):
        return self.nome
    
    def getMatricola(self):
        return self.matricola
    

    def getCorso(self, matricola):
        for corso in self.corsi:
            if matricola == corso.getMatricola():
                return f"{corso.getNome()}  {corso.getMatricola()}  {corso.getDurata()}"  
        raise('Corso non trovato')

    def getListaCorsi(self):
        for corso in self.corsi:
            print(f'{corso.getNome()}  {corso.getMatricola()}  {corso.getDurata()}')

    def addCorso(self, corso):
        self.corsi.append(corso)


    def getStudente(self, matricola):
        for studente in self.studenti:
            if matricola == studente.getMatricola():
                return f"{studente.getNome()}  {studente.getMatricola()}"
        raise('Studente non trovato')    

    def getListaStudenti(self):
        for studente in self.studenti:
            print(studente.getNome() + studente.getMatricola())

    def addStudente(self, studente):
        self.studenti.append(studente)


    def getDocente(self, matricola):
        for docente in self.docenti:
            if matricola == docente.getMatricola():
                return f"{docente.getNome()}  {docente.getMatricola()}"
        raise('Docente non trovato')
    
    def getListaDocenti(self):
        for docente in self.docenti:
            print(docente.getNome() + docente.getMatricola())

    def addDocente(self, docente):
        self.docenti.append(docente)