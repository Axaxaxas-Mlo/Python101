class instrumento:
    def __init__ (self, precio):
        self.precio = precio
    
    def tocar(self):
        print('Estamos tocando musica')

    def romper(self):
        print('Eso lo pagas tu, son', self.precio, 'pesos')

class bateria(instrumento):
    pass

class guitarra(instrumento):
    def __init__(self, precio, cuerdas):
        self.precio = precio # porque tenemos que volver a definir precio? si no lo hacemos busca en el padre
        self.cuerdas = cuerdas # nueva variable o valor que difiere de Instrumento
        self.romper() # llama el metodo romper de la clase guitarra en cuanto se inicializa un objeto Guitarra.
        super().romper()  # obliga a ir a buscar ese metodo en el padre y lo llama al parecer, pero porque?
    
    def romper(self):
        print('Romper la guitarra') # define un nuevo metodo de romper

#mi_guitarra = guitarra(300,4)
#mi_guitarra.tocar()
#mi_guitarra.romper()

# print(type(mi_guitarra)) # <class '__main__.guitarra'>

otra_guitarra = guitarra(200,5)
#otra_guitarra.tocar()
otra_guitarra.romper()