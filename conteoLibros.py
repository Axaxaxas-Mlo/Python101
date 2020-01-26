import operator

libro = open ('The Last Man2.txt', 'r') # uso la version cortada, la original tarda mucho
conteo_palabras = {}

for linea in libro:
    lineas = (linea.split())
    #print(lineas)
    for i in lineas:
        #print(i)
        if i in list(conteo_palabras.keys()):
            conteo = conteo_palabras.get(i)
            palabra = {i : conteo + 1}
            conteo_palabras.update(palabra)
            #print(conteo_palabras)
        else:
            palabra = {i : 1}
            conteo_palabras.update(palabra)
            #print(conteo_palabras)

for k, v in conteo_palabras.items():
    print(k + '-' + str(v))

alphabet = frozenset('abcdefg')
print (alphabet)
# se guardaa???
# print(sorted(conteo_palabras, key = conteo_palabras.get(), reverse = True))  # no se como ordenarlo
#print(conteo_palabras)