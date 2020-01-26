Lista1 = ['Elemento 1',2]
print(Lista1)
print(type(Lista1[0]))

cuadrados = [1,4,9,16,25]
print(cuadrados)

slice = cuadrados[:-1] # No entiendo bien como funciona, si es una clase porque se define asi?
print(slice)            # Slice realmente es una lista, que onda con esto?

cuadrados[2] = 'dos'
print(cuadrados)
 

animales = ['elefante', 'leon', 'tigre', 'jirafa']
print(animales)

animales += ['mono', 'perro'] # similar a B = B + [Elem1,Elem2]
print(animales)

animales.append('dino') # anades solo un elemento al final de la lista
print(animales)

animales[6] = 'Dinosaurio' # solo modificas un solo elemento [6]
print(animales)

animales = animales + ['gato', 'pajaro'] # parecido al append pero puedes agregar mas de un elemento
print(animales)

plantas = ['arbustos','flores']
animales += [plantas,2]
print(animales)

Ultimo = animales.pop()
print(Ultimo)

animales[2:3] = ['gato pequeno', 'gato grande'] # puedes remplazarlo por un mismo elemento 'gato' en ambos elementos
print(animales)

animales[3:5] = []
print(animales)

#animales[:] = [] # igual sirve para borrar la lista
#print(animales)

animales.clear() # metodo para borrar una lista
print(animales)

grocery_list = ['pescado', 'tomate', 'manzana']
print('tomate' in grocery_list) # la funcion in sirve para buscar un elemento en una lista, en que mas sirve?