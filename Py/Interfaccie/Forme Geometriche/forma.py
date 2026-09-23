from abc import abstractmethod, abstractclass

@abstractclass
class Forma:

    @abstractmethod
    def calcoloArea(self) -> int:
        pass

    @abstractmethod
    def calcoloPerimetro(self) -> int:
        pass

    @abstractmethod
    def numeroAngoli(self) -> int:
        pass
        
    @abstractmetod
    def info(self) -> str:
    	return f'area : {self.calcoloArea()}, perimetro : {self.calcoloPerimetro()}, angoli : {self.numeroAngoli()}'
