class Rubrica:
    
    # Builder
    def __init__(self, dizionario) -> None:
        self.dizionario = dizionario

    # Utility
    def importaFile(self, file):
        self.dizionario = {}
        with open(file, 'r') as fin:
            while True:
                line = fin.readline()
                if line == '':
                    break
                self.dizionario[line.split(' : ')[0]] =  line.split(' : ')[1].split(' ')[0]


    def salvaFile(self, file):
        with open(file, 'w') as fout:
            for nome, email in self.dizionario.items():
                fout.write(f'{nome} : {email} \n')

    def addContatto(self, key, value):
        self.dizionario[key] =  value

    def getDizionario(self):
        for key, value in self.dizionario.items():
            print(f'{key} : {value}')

        return ''

    def getIniziale(self, char):
        for key in self.dizionario.items():
            if key.split(' ')[1][0] == char:
                print(key)

        return ''

    def getBenvenuto(self, char):
        for key, value in self.dizionario.items():
            if key.split(' ')[1][0] == char:
                print(f'Ciao {key}, il tuo indirizzo email {value}')

        return ''