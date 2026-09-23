from biblioteca import Biblioteca
from autore import Autore
from libro import Libro

def init():

    a1 = Autore('Dante', 'Alighieri')
    a2 = Autore('Bella', 'Bro')
    
    l1 = Libro('Divina commedia', a1, 1200)
    l2 = Libro('Libro bello', a2, 2022)
    l3 = Libro('libro figo', a2, 2023)
    
    b = Biblioteca('Vez')

    b.addLibro(l1)
    b.addLibro(l2)
    b.addLibro(l3)
    
    print(b.getListaLibri())

    print(b.getListaAutore(a1))
    
init()