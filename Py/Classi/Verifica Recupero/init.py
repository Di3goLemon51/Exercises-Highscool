from prestito import Prestito
from utente import Utente
from libroDigitale import LibroDigitale
from libroCartaceo import LibroCartaceo

def init():
    
    u1 = Utente('Carlo', 'Erba')
    l1 = LibroCartaceo('Commedia', 'Dante', 1200, 2000)
    l2 = LibroDigitale('Barzellete', 'Carlo', 2022, '.pdf')

    pres1 = Prestito(l1, u1, '18/5/23', '18/6/23')
    pres2 = Prestito(l2, u1, '16/5/23', '16/6/23')
        
    print(u1.getInfo())
    print(l1.getInfo())
    print(l2.getInfo())
    print(pres1.getInfo())
    print(pres2.getInfo())

init()