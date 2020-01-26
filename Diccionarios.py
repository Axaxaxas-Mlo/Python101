dct = {1 : 'primer valor', 2 : 'segundo valor'}

print(dct[2])

phone_book = {'john' : 123, 'Juan' : 456, 'Maria' : 789,}
print(phone_book)

phone_book['Jill'] = 246
print(phone_book)

del phone_book['john'] # Esta funcion no viene en la pagina, no se porque o como funciona
print(phone_book)

print(phone_book['Maria'])

print(phone_book.keys())
print(phone_book.values())

#lstkeys = phone_book.keys()
listakeys = list(phone_book.keys())
print(listakeys)

listavalues = list(phone_book.values())
print(listavalues)

dicttotupla = zip(listakeys,listavalues) # creamos un iterable de tuplas con las dos listas
listDicttoTupla = list(dicttotupla) # creamos una lista con el iterable
print(listDicttoTupla) # imprimimos la lista.

grocery_dict = {'pescado':1,'tomate':4,'manzana':8}
print(1 in grocery_dict.values())