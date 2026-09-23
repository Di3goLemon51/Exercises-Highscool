# n = 5 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14

# versione iterativa
def triangolo(n):

    c = 1

    for i in range(n + 1):      # contatore per le righe
        for j in range(i):      # contatore elementi per riga

            print(c, end= ' ')
            c += 1

        print()     # a capo


# versione ricorsiva
def triangoloRicorsivo(n, x = 0, c = 1):

    if x == n:
        return 1
    
    else:
        for i in range(x + 1):
            print(c, end= ' ')
            c += 1

        print()

        return triangoloRicorsivo(n, x + 1, c)



# print con init
def __init__():
    triangolo(5)
    print()
    triangoloRicorsivo(5)

__init__()