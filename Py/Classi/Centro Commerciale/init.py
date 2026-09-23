from negozio import Negozio
from centro import Centro

def init():

    nave = Centro('Nave de Vero')

    ovs = Negozio('OVS', '00', 'Abbigliamento')
    nave.addNeg(ovs)
    ovs.addProd('maglietta blu', '001', 7.99)

    alcoot = Negozio('Alcoot', '01', 'Abbigliamento')
    nave.addNeg(alcoot)
    alcoot.addProd('pantalone verde', '002', 17.99)

    kfc = Negozio('KFC', '02', 'FastFood')
    nave.addNeg(kfc)
    kfc.addProd('Pollo Fritto', '003', 11.99)

init()