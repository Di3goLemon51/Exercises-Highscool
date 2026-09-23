# Es 3
class Calcolatrice:

    # Costruttore
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Utility
    def addizione(self,):
        return self.a + self.b
    
    def sottrazione(self):
        return self.a - self.b
    
    def moltiplicazione(self):
        return self.a * self.b
    
    def divisione(self):
        return self.a / self.b
    

operazione = Calcolatrice(6, 2)
print(operazione.addizione())
print(operazione.sottrazione())
print(operazione.moltiplicazione())
print(operazione.divisione())