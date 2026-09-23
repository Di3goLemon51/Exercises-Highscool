from persona import Persona

class Docente(Persona):

    def __init__(self, nome, matricola):
        super().__init__(nome, matricola)