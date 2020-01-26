archivo = open('paises.txt','r')
paises = []

for linea in archivo:
    paises.append(linea.strip())
archivo.close

print(paises)
print(len(paises))

for pais in paises:
    if pais[0] == 'M':
        print(pais)