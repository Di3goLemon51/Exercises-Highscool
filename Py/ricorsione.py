# Es 1 Calcolare il fattoriale di un numero.
def fattoriale(n):

    if n != 0:
        return n * fattoriale(n-1)

    else:
        return 1
    
    
# Es 2 Calcolare la somma di una lista.
def sommaLista(ls):

    if len(ls) == 0:
        return 0
    
    else:
        return ls[0] + sommaLista(ls[1:]) 
    

# Es 3 Calcolare la sequenza di Fibonacci.
def fibonacci(n):

    if n <= 1:
        return n
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Es 4 Calcolare la potenza.
def potenza(x, y):

    if y == 0:
        return 1
    
    else:
        return x * potenza(x, y - 1)


# Es 5 Calcolare il massimo comune divisore (MCD).
def MCD(x, y):

    if x - y == 0:
        return y
        
    else:
        if x < y:
            x, y = y, x

        elif x == y:
            return y

        else:
            x -= y

        return MCD(x, y)


# Es 6 Stampare numeri da 1 a N.
def stampa(n):

    if n == 1:
        return 1
    
    else:
        print(n, end=' ')
        return stampa(n - 1)


# stampa
def init():
    print(fattoriale(5))
    print(sommaLista([1, 2, 3, 4]))
    print(fibonacci(6))
    print(potenza(3, 3))
    print(MCD(6, 9))
    print(stampa(5))

init()