# lista de paises en 
# guardar un archivo llamado paises.txt

archivo = open('paises.txt', 'r')

for linea in archivo:
    print(linea.strip())

archivo.close