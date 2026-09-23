from forma import Forma

class Triangolo(Forma):

    def __init__(self, lato) -> None:
        self.l = lato
        self.h = sqrt(lato ** 2 - lato / 2 ** 2)

    def calcoloArea(self):
        return self.l * self.l / 2
    
    def calcoloPerimetro(self):
        return self.l * 3
    
    def numeroAngoli(self):
        return 3
        
    def info(self):
    	super().info()
