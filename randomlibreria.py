import random

# lista = [1,2,3,4,5,6]

# print(random.choice(lista))

estados = {'Guanajuato':'guanajuato', 'Jalisco':'Guadalajara','Nuevo Leon':'Monterrey'}

#print(estados)
estado = random.choice(list(estados))
#print('Capital de ' estado)
#print ('Capital de %s : ' %estado)
capital = input('Capital de ' + estado + ': ')

#print (capital)

if capital == estados[estado]:
    print('correcto')
else:
    print ('Incorrecto') # no me salio, no se que onda
                        # ya me salio, el detalle fue en la linea 17, la 13 no me da problemas
