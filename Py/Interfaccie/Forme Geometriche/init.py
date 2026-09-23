from triangolo import Triangolo
from rettangolo import Rettangolo
from trapezio import Trapezio
from cerchio import Cerchio

def init():

    tri = Triangolo(3)
    print(tri.info())
    
    print()
    
    ret = Rettangolo(5, 3)
    print(ret.info())
    
    print()
    
    trap = (5, 3, 2, 2)
    print(trap.info())
    
    print()
    
    cer = Cerchio(4)
    print(cer.info())
