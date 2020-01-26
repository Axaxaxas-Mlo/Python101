import operator

def limpia_puntuacion(palabra, puntuacion):
    palabra_limpia = ''
    if puntuacion in palabra:   # si el signo no esta en la palabra, no hagas nada
        for i in palabra:       # si si tiene un signo, revisa cada char
            if not i == puntuacion: # si no es el signo, si agregalo, si es el signo, ignoralo.
                palabra_limpia += i # No entiendo esta parte // ya, no era un uno, agregas el char que no sea el signo
    else:
        palabra_limpia = palabra
    return palabra_limpia



def limpia_palabra(palabra):
    palabra = limpia_puntuacion(palabra,',')
    palabra = limpia_puntuacion(palabra,';')
    palabra = limpia_puntuacion(palabra,'.')
    palabra = limpia_puntuacion(palabra,':')
    palabra = limpia_puntuacion(palabra,'(')
    palabra = limpia_puntuacion(palabra,')')
    palabra = palabra.lower()
    return palabra

libro = open ('The Last Man2.txt', 'r') # uso la version cortada, la original tarda mucho
conteo_palabras = {} # creamos el dict vacio.

for linea in libro: # para cada linea del libro
    lineas = (linea.split()) # crea una lista, cada elemento es una de las palabras de la linea
    #print(lineas)
    for i in lineas: # para cada elemento (palabra) de la linea
        i = limpia_palabra(i) # tomamos cada elemento (palabra) de la linea y la limpiamos
        #print(i)
        if i in list(conteo_palabras.keys()): #revisa si la palabra esta en el dict
            conteo = conteo_palabras.get(i) # si si esta, dame el conteo actual de esa palabra
            palabra = {i : conteo + 1} # crea un dict temporal sumando uno al conteo
            conteo_palabras.update(palabra) # y actualiza la palabra con el nuevo conteo
            #print(conteo_palabras)
        else:
            palabra = {i : 1} # si no esta la palabra en el dict
            conteo_palabras.update(palabra) #  agregala con 1 en el conteo
            #print(conteo_palabras)

libro.close() # cerramos el libro, ya llenamos el dict

# for k, v in conteo_palabras.items(): # para cada item del dict
#     print(k + '-' + str(v)) # imprimeme los keys y los valores, no se porque sirve

palabras_lista = [for i in conteo_palabras.get()]
palabras_ordenadas = sorted(conteo_palabras, key = conteo_palabras.get(), reverse = True)  # no se como ordenarlo
#print(conteo_palabras)