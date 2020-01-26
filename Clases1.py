class MiClase(object): # creamos una clase, una clase es como un template, un blueprint para crear Objetos
    variable = 10 # dentro de la clase podemos definir variables
    def saluda(self): # o funciones
        print('Hola desde la funcion saluda')

mi_objeto = MiClase() # creamos un objeto de clase MiClase
mi_objeto.saluda() # llamamos la funcion 'saluda' de la clase MiClase
print(type(mi_objeto)) # devuelve: <class '__main__.MiClase'>
#Edicion1
#Edicion2
#Edicion3
#Edicion4