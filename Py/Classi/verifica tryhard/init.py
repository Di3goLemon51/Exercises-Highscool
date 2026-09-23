from scuola import Scuola
from corso import Corso
from studente import Studente
from docente import Docente

def init():

    morin = Scuola('Liceo Ugo Morin', '01')

    info = Corso('Informatica', '001', 'Semestrale')
    morin.addCorso(info)
    mate = Corso('Matematica', '002', 'Annuale')
    morin.addCorso(mate)
    fisica = Corso('Fisica', '003', 'Annuale')
    morin.addCorso(fisica)

    giorgio = Studente('Giorgio Bassano', '0001')
    morin.addStudente(giorgio)
    giorgio.addCorso(info)
    giorgio.addCorso(mate)

    giorgio.addVoto(9)
    giorgio.addVoto(7)
    giorgio.addVoto(8)
    giorgio.getMediaVoti()

    kevin = Docente('Kevin Gemolo', '0002')
    morin.addDocente(kevin)
    kevin.addCorso(info)

    franco = Studente('Franco Vescovi', '0003')
    morin.addStudente(franco)
    paolo = Docente('Paolo Rossi', '0004')
    morin.addDocente(paolo)

    print(morin.getListaCorsi())
    print(morin.getCorso('003'))

    print(morin.getListaStudenti())
    print(morin.getStudente('0001'))
    print(giorgio.getListaCorsi())
    print(giorgio.getMediaVoti())

    print(morin.getListaDocenti())
    print(morin.getDocente('0004'))

init()