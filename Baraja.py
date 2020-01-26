import random

class baraja():
    def __init__(self):
        palo =  ['corazones', 'espadas', 'diamantes', 'trebol']
        numero = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] # As, 2-10, J, Q, K
        crear_baraja = []
        
        for i in numero:
            for j in palo:
                crear_baraja.append(str(i) + ' de ' + str(j))
        #print(crear_baraja)
        self.crear_baraja = crear_baraja

    def barajear(self):
            random.shuffle(self.crear_baraja)
        #print(self.crear_baraja)

    def repartir(self): # repartir carta random
        if len(self.crear_baraja) == 0:
            print ('Ya no quedan cartas para repartir')
        else:
            print(self.crear_baraja.pop(0))
            print('Quedan', str(len(self.crear_baraja)), 'cartas en la baraja')

    def mostrar(self):
        print(self.crear_baraja)

baraja1 = baraja()
baraja1.barajear()

for i in range(56):
    baraja1.repartir()

# baraja1.repartir()
# baraja1.repartir()

baraja1.mostrar()

