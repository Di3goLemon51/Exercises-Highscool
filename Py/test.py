class Scuola:
    
    def __init__(self, nome, codice) -> None:
        self.nome = nome
        self.codice = codice
        self.corsi = []
        
    #metodo per inserire un corso alla lista dei corsi
    def inserisciCorso(self, nome, matricola, durata):
        # Istanziamo l'oggetto
        corso = Corso(nome, matricola, durata)
        self.corsi.append(corso)
    
    def printCorsi(self):
        for corso in self.corsi:
            print("nome: " + corso.nome + "  matricola: " + corso.matricola + "   durata:" + corso.durata)
    
    def getCorso(self, matricola):
        for corso in self.corsi:
            if corso.getMatricola() == matricola:
                return corso
        raise("Il corso non esiste")
    
class Corso:
    
    # Costruttore
    def __init__(self, nome, matricola, durata):
        self.nome = nome
        self.matricola = matricola
        self.durata = durata
    
    # Getters
    def getNome(self):
        return self.nome
    
    def getMatricola(self):
        return self.matricola
    
    def getDurata(self):
        self.durata
    
    # Setters
    def setNome(self, nome) -> None:
        self.nome = nome
    
    def setMatricola(self, matricola) -> None:
        self.matricola = matricola
    
    def setDurata(self, durata) -> None:
        self.durata = durata


class Persona:
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        self.name = name
        self.surname = surname
        self.matricola = matricola
        self.corsi = []
    
    def inserisciCorso(self, corso):
        self.corsi.append(corso)
        
    def getCorso(self, matricola):
        for corso in self.corsi:
            if corso.getMatricola() == matricola:
                return corso
        raise("Il corso non esiste")
    
    # Getters
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getMatricola(self):
        return self.matricola
    
    # Setters    
    def setName(self, name):
        self.name = name
    
    def setSurname(self, surname):
        self.surname = surname
    
    def setMatricola(self, matricola):
        self.matricola = matricola
    

class Studente(Persona):
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        super().__init__(name, surname, matricola)

class Docente(Persona):
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        super().__init__(name, surname, matricola)


def init():
    scuola = Scuola("Liceo Morin", "00")
    scuola.inserisciCorso("Informatica", "00", "Annuale")
    scuola.inserisciCorso("Matematica", "01", "Annuale")
    scuola.inserisciCorso("Fisica", "02", "Trimestre")
    scuola.inserisciCorso("Italiano", "03", "Pentamestre")
    
    informatica = scuola.getCorso("00")
    
    kevin = Docente("Kevin", "Gemolo", "00000")
    
    kevin.inserisciCorso(informatica)
    print(kevin.getCorso("00"))
    
    marco = Studente("Marco","f", "22")
    marco.inserisciCorso(informatica)
    
init()    