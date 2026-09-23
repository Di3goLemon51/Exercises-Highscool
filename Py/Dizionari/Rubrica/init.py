from rubrica import Rubrica

def init():

    rubrica = Rubrica({})
    rubrica.importaFile('input.txt')

    rubrica.addContatto('Jabob Ballico', 'justino@liceojustin.noob')
    rubrica.addContatto('Carlo Teodor', 'carlo.teddy@stunnato.com')
    rubrica.salvaFile('output.txt')

    print(rubrica.getBenvenuto('B'))
    print(rubrica.getDizionario())

init()