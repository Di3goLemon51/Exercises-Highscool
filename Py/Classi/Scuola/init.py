from docente import Docente
from studente import Studente
from scuola import Scuola

def init():
    morin = Scuola('Liceo Ugo Morin')
    morin.addCorso('Economia', '0001', 'Annuale')
    morin.addCorso('GrecoAntico', '0002', 'Biennale')
    morin.addCorso('Informatica', '0003', 'Annuale')

    alCarlo = Studente('Carlo', 'Teodoro', '104104')
    morin.addStudente('Carlo', 'Teodoro', '104104')
    alCarlo.addCorso('Economia', '0001', 'Annuale')
    alCarlo.addCorso('GrecoAntico', '0002', 'Biennale')
    alCarlo.getCorsi()

    doDandro = Docente('Dandro', 'Soro', '1001')
    morin.addDocente('Dandro', 'Soro', '1001')
    doDandro.getNome()
    doDandro.getCognome()
    doDandro.addCorso('Informatica', '0003', 'Annuale')

    morin.getNome()
    morin.getCorsi()
    morin.getDocenti()
    morin.getStudenti()

init()