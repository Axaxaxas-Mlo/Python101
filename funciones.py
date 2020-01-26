def hola_mundo():
    print('hola mundo')

for i in range(5):
    hola_mundo()    #llama la funcion hola mundo 5 veces.

# Quiero ser una funcion.

def fun():
    print('Quiero ser una funcion.')

for i in range(5):
    fun()

def algo (x):
    print ('x = ' + str(x))

algo(5)

def cuadrado(x):
    print(x**2)

#input('Dame el cuadrado de: ' )
cuadrado(int(input('Dame el cuadrado de: ' ))) # si funciona bien, toma el valor y lo corre.

def suma_2_numeros (a,b):
    return a +b

#c = suma_2_numeros(2,4) # 
print(suma_2_numeros(2,4))

def fib(n):
    """
    Esta es la documentacion que aparece cuando llamas esta funcion
    """
    resultado = []
    a = 1
    b = 0
    #while a < n:



#fib()

# como definir parametros default al llamar una funcion.

def multiplica_por (a, b = 2):
    return a * b

print(multiplica_por(3,3))
print(multiplica_por(8))

def hola (sujeto = 'Python', nombre = 'Andres'):
    print ('Hola %s mi nombre es %s' % (sujeto, nombre))

hola('C++')