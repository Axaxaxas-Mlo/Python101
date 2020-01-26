print ("Hola, este es el programa sobre variables")
a = 2
#print(a)
a = b = 2
#print(a)
#print(b)
#la expresion str se usa para convertir las var a y b de int a str
print("a = " + str(a))
print("b = " + str(b))

saludos = "saludos"
print("saludos = " + str(saludos))
saludos = 123
print("saludos = " + str(saludos))
print(type(saludos))
print(isinstance(saludos,(int,str)))
print(isinstance(saludos,str))
print(type([]))