frase = """
Esta es una cadena muy larga los tres 
caracteres de comillas son utilizados 
para definir cadenas multilineas
"""

first_half = frase[:int(len(frase)/2)]
print(first_half)

print("         ")
second_half = frase[int(len(frase)/2):]
print(second_half)