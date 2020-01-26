print('hola mucho gusto'[3:-1]) # toma del 3 hasta el fin -1
print('hola mucho gusto'[:]) # toma del inicio hasta el fin
print('hola mucho gusto'[:-2]) # toma del inicio hasta el fin - 2
print('hola mucho gusto'[4:]) # toma del 4 hasta el fin

monty_python = 'Monty python'
monty = monty_python[:5]
print(monty)

python = monty_python[-6:]
print(python)
python.capitalize() # No se como funciona los metodos en string, sale igual.
print(python.capitalize()) #ya vi como funciona, parecido a str o int, solo lo hace para esa instancia, no lo redefine

"""
Comentario? al parecer, no me parece muy recomendable pero funciona
"""