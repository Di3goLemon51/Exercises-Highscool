#1. Scrivi una funzione per il fattoriale ricorsivo

def fattorialeRicorsivo(n):

    if n != 0:
        return n * fattorialeRicorsivo(n-1)

    else:
        return 1
            
#2. Scrivi una funzione Python che accetti un numero intero e restituisca True se il numero è un numero primo, 
# altrimenti restituisca False.

def primo(n):

    if n % 2 == 0:
        return False

    for i in range(3, n-1):
        if n % i == 0:
            return False
        
    return True

#3. Dato una lista di 10 numeri fai un codice che la ordini (crescente o decrescente)

def ordina(l):

    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]

    return l

'''
4. Cosa fa il seguente codice Python?
Crea una nuova lista dove ogni numero è il doppio rispetto alla lista iniziale.
'''

#6. Fai una funzione che trova la somma del triangolo superiore ed inferiore di una matrice NxN




#7. Fai una funzione che faccia la trasposta di una matrice ovvero da una matrice NxM diventa MxN
def trasposta(m):

    mT = []

    for c in range(len(m[0])):
        mT += [[m[r][c] for r in range(len(m))]]

    return mT

#stampa di tutto
def init():
    print(fattorialeRicorsivo(5))
    print(primo(7))
    print(ordina([3, 5, 7, 2, 6, 1, 9, 4, 8, 10]))
    print(trasposta([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

init()