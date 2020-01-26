class persona(object): # El object no es a fuerzas, no entiendo bien
    """ Esta es la documentacion de la clase persona """
    def __init__ (self,name): # Siempre se pone, funcion de inicializacion, definimos name dentro de Persona
        self.name = name # variable de instancia

    def saluda (self):
        print ('Hola ' + self.name) # no entienco cual es la ventaja de usar self.name sobre name
    
    def despidete (self):
        print ('Adios ' + self.name)

p = persona('Ana')
p.saluda()
p.despidete()


j = persona('Jessica')
j.saluda()
j.despidete()