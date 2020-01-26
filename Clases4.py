class coche:
    """     Abstraccion de los objetos coche """
    def __init__(self,gasolina):
        self.gasolina = gasolina
        print ('Tenemos', gasolina, 'litros') # si imprime asi, me pone un espacion entre los str

    def arrancar (self):
        if self.gasolina > 0:
            print ('Arranca')
        else:
            print ('No Arranca')
    
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ('Quedan', self.gasolina, 'litros')
        else:
            print ('No se mueve')
    # def cargar_gas(self):
    #     self.gasolina


print('recuerda que para salir debes dar enter') # me gusta esta forma de tener el programa abierto hasta 
while True:     # que des enter, todo el programa dentro del ciclo while funciona bien.
    gasolina = int(input('Ingresa la gasolina que tendra tu vochito: '))
    distancia = int(input('Que tanto quieres manejar?: '))
    vochito = coche(gasolina)
    vochito.arrancar()
    for i in range(distancia):
        vochito.conducir()