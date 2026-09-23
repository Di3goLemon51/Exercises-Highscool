from autoElettrica import AutoElettrica
from motoElettrica import MotoElettrica

def init():
    tesla = AutoElettrica('Tesla', 'X', 1000)
    print(tesla.stampaAutonomia())

    moto = MotoElettrica('Yamaha', 'RM1', 500)
    print(moto.stampaAutonomia())

init()