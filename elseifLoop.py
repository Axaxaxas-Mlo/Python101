x = -2

if x < 0:
    print ('x < 0') # checa si es menor a cero
elif x == 0:
    print ('x is zero') # si no es verdadero que x < 0, checa si x = 0
elif x == 1:
    print ('x is one') # si no es igual a cero, checa si es uno
else:
    print ('Ninguno de los anteriores es verdadero') # cuando ningun valor es correcto

name = 'ana'

if name in 'panama':
    print ('Si esta')
else:
    print ('No esta')

a = 2
b = 3

if a < b:
    print ('a es menor que b')
elif a == b:
    print ('a es igual a b')
else:
    print ('a es mayor que b')

c = 4

"""
if a < b and a < c:
    if b < c:
        print ('a < b < c')
    else:
        print ('a < c < b')
elif a < b and a > c:
    print ('b < a < c')
elif a > b and a < c:
    if b < c:
        print
"""

temp = 31

if temp > 22 and temp < 30:
    print ('temperatura esta bien (%d)' %temp)
else:
    print ('temperatura esta mal (%d)' %temp)

temp = 31

if  22 <= temp <= 30:
    print ('temperatura esta bien (%d)' %temp)
else:
    print ('temperatura esta mal (%d)' %temp)


temp = int(input('Introduzca la temperatura actual'))
if  22 <= temp <= 30:
    print ('temperatura esta bien (%d)' %temp)
else:
    print ('temperatura esta mal (%d)' %temp)
