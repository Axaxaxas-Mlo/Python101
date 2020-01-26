archivo = open ('datos.csv', 'w') # Si no existe lo crea, si ya existe lo sobre-escribe

while True:
    persona = input ('Nombre de la persona: ')

    if persona == 'salir':
        print ('Adios')
        break
    else:
        datos = input ('Datos de ' + persona + ': ')
        archivo.write (persona + ', ' + datos + '\n')

# print(archivo.tell()) # se supone que te da la direccion pero me da un numero
archivo.close