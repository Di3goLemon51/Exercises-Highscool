from forma import Forma

class Rettangolo(Forma):

    def __init__(self, raggio) -> None:
        self.r = raggio
	self.pi = 3.14

    def calcoloArea(self):
        return round(self.pi*self.r**2, 2)
    
    def calcoloPerimetro(self):
        return round(self.pi*self.r*2, 2)
    
    def numeroAngoli(self):
        return 0
        
    def info(self):
    	super().info()
