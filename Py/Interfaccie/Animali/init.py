from cane import Cane
from cavallo import Cavallo
from leone import Leone
from random import randint, choice
from time import sleep

def init():
    
    nomiAnimali = ['Leo', 'Fido', 'Rex', 'Fluffy', 'Shadow', 'Simba', 'Luna', 'Bella', 'Carlo']
    listaAnimali = []
    a = randint(1, 10)

    for _ in range(a):
        b = randint(1, 3)
        nome = choice(nomiAnimali)
        età = randint(1, 15)

        if b == 1:
            razza = choice(['Pastore Tedesco', 'Bassotto', 'Golden Retriever'])
            var = Cane(nome, età, razza)
        
        elif b == 2:
            mantello = choice(['Bianco', 'Nero', 'Marrone', 'Misto'])
            var = Cavallo(nome, età, mantello)

        elif b == 3:
            peso = randint(50, 200)
            var = Leone(nome, età, peso)
        
        listaAnimali.append(var)

    for _ in range(20):
        anim = choice(listaAnimali)
        print(f'Nome: {anim.getNome()}, Età: {anim.getEtà()}, Attributo: {anim.info()}')

        c = randint(1, 5)

        if c == 1:
            print(anim.parla())

        elif c == 2:
            print(anim.muove())

        elif c == 3:
            print(anim.mangia())

        elif c == 4:
            print(anim.beve())

        elif c == 5:
            sonno = randint(1, 10)
            print(anim.dorme(sonno))

        sleep(2)

init()