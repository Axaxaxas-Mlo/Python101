# count = 0

# while True:
#     print (count)
#     count += 1
#     if count >= 5:
#         break   # seems unnecessary but ok

# zoo = ['lion', 'tiger', 'elephant']

# while True:
#     animal = zoo.pop() # saca el ultimo elemento de zoo
#     print (animal)
#     if animal == 'tiger': # si animal es tiger, termina el ciclo.
#         break

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# for x in range (10):
#     if x%2 == 0:
#         continue
#     print(x)

# nombres = ['paco', 'luis', 'hugo']

# for nombre in nombres:
#     print(nombre)

# for nombre in nombres:
#     print ('Hola %s' %nombre)

# nombres += ['ana','andres','elsa','oscar','umberto','isabel']
# vocales = ['a','e','i','o','u'] # puede ser un string = 'aeiou' e igual funciona
# print(nombres)

# for nombre in nombres:
#     if not (nombre[0] in vocales):
#         continue
#     print (nombre)

# for nombre in nombres:
#     if nombre[0] in vocales:
#         print (nombre)

# precios = [12.5,3.14,8.44,0.98]
# total = 0

# for precio in precios:
#     total += precio

# print ('el precio total es %f' %total)
# print ('el precio total es %s' %total)
# print ('el precio total es ' + str(total))


while True:
    user_input = input('>  ')
    if user_input == 'salir':
        print ('adios')
        break
    else:  
        print (user_input)
