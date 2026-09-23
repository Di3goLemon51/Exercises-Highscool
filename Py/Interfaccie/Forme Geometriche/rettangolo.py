from forma import Forma

class Rettangolo(Forma):

    def __init__(self, base, altezza) -> None:
        self.b = base
        self.h = altezza

    def calcoloArea(self):
        return self.b * self.h
    
    def calcoloPerimetro(self):
        return (self.b + self.h) * 2
    
    def numeroAngoli(self):
        return 4
        
    def info(self):
    	super().info()
