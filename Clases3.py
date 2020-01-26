import random

class Dado():
    def __init__(self,lados):
        self.lados = lados
    def tirar(self):
        return random.randint(1,self.lados)

dado6 = Dado(6)  # new? no entiendo eso, osea si entiendo que crea uno nuevo pero que onda?

for i in range(6):
    print (dado6.tirar())

dado12 = Dado(12) # creamos el objeto con 12 lados, por eso si ocupamos el __init__ en la clase
dado24 = Dado(24) # tenemos que definir los lados al crear el objeto, ya despues no se puede modificar.

for i in range(2):
    print (dado12.tirar())
    print (dado24.tirar())