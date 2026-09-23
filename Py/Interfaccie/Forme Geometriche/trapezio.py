from forma import Forma

class Rettangolo(Forma):

    def __init__(self, baseMin, baseMag, altezza, latoObliquo) -> None:
        self.b1 = baseMin
        self.b2 = baseMag
        self.h = altezza
        self.l = latoObliquo

    def calcoloArea(self):
        return (self.b1 + self.b2) * self.h / 2
    
    def calcoloPerimetro(self):
        return self.b1 + self.b2 + self.l * 2
    
    def numeroAngoli(self):
        return 4
        
    def info(self):
    	super().info()
