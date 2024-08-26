#practica RECURSION

#ejercicio 1:
#Escriba una función recursiva repite_hola que reciba como parámetro un número entero n y
#escriba por pantalla n veces el mensaje "Hola". Invóquela con distintos valores de n:

def repite_hola(n: int) ->str:
    #caso base:
    if n ==0:
        return None
    else:
        print("hola")
        return repite_hola(n-1)

a = repite_hola(6)
print(a)

def repite_hola(n: int) ->str:
    #caso base:
    if n ==0:
        return None
    else:
        return"hola", repite_hola(n-1)

b= repite_hola(6)
print(b)

# que hace la funcion:
def misterio(a: int) -> int:
    if a == 0:
        return a
    return 1 + misterio(a - 1)

c = misterio(2)
print(c)

# Considere la siguiente función recursiva:
def f(n, d):
    if n > 1:
        if n % d == 0:
            print(d)
            f(n // d, d)
        else:
            f(n, d + 1)

e = f(30,2)
print(e)

#funcion iterativa:
def iterativa(n, d):
    factores = []
    while n > 1:
        if n % d == 0:
            factores.append(d)
            n //= d  # Dividimos n por d si es divisible
        else:
            d += 1  # Probamos con el siguiente número si no es divisible
    return factores

print(iterativa(18, 2))  # Output: [2, 3, 3]


#otro caso:
def mystery(a: int, b: int) -> int:
    if (b == 0):
        return a
    return mystery(2 * a, b - 1)


result = mystery(7, 3)
print(result)

#Escriba una función recursiva que tome un numero natural n e imprima todos los números desde n
#hasta 1.

def recu(n:int) -> int:
    if n == 0:
        return 
    else:
        return n, recu(n-1)
    
z = recu(5)
print(z)


#Ejercicio 7
#Convierta la siguiente función recursiva a una iterativa.
def recursiva(t: int, k: int) -> int:
    if t >= 100:
        return k
    else:
        return recursiva(t + k, k + 1)
    

    
a = recursiva(10,5)
print(a)    
    

def iterativa(t: int, k:int) ->int:
    while t <= 100:
        t +=k #incremento t en k
        k +=1  # incremento de a 1 en k
    return k


s = iterativa(3,2)
print(s)

# Ejercicio 8
#Escriba una función recursiva que calcule el n-ésimo número triangular (el número 1 + 2 + 3 + ...+ n).

def enesimo(n: int) ->int:
    if n == 0:
        return n
    else:
        print(n)
        return n + enesimo(n -1)
    
ene = enesimo(5)
print(ene)

# Ejercicio 9
#Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def digitos (n: int) -> int:
    if n == 0:
        return 0
    else:
        return 1 + digitos(n // 10) 
    
dig = digitos(500)
print(dig)


# Ejercicio 10
#Escriba una función recursiva que reciba 2 enteros n y b y devuelva True si n es potencia de b.
def potencia(n: int, b: int) -> bool:
    # Caso base 1: Si n es 1, entonces n es una potencia de b (b^0 = 1).
    if n == 1:
        return True
    
    # Caso base 2: Si n no es divisible por b, n no es una potencia de b.
    if n % b != 0 or n == 0:
        return False
    
    # Llamada recursiva: divide n por b y repite el proceso.
    return potencia(n // b, b)

# Ejemplo de uso
pot = potencia(8, 2)
print(pot)  # Debería devolver True, ya que 8 es 2^3


potencia(8, 2) 
potencia(64, 4)
potencia(70, 10) 


# Ejercicio 11: encontrar el mayor elemento de una lista
def mayor_lista(l: list) ->int:
    if len(l) ==0:
        return "lista vacia"
    elif len(l) == 1:
        return l[0]
    else:
        max = mayor_lista(l[1:])
        if l[0] > max:
            return l[0]
        else:
            return max
        
a = [1,5,3,6,9,7]
lista = mayor_lista(a)
print(lista)
        
#ejercicio 12:  convertir esta funcion en una recursiva:
#multiplica los elementos de una lista
def iterativa(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c


a = [1,5,3,6,9,7]

h = iterativa(a)
print(h)

def recursiva(l: list[int]) -> int:
    #caso base: #anda bien
    if len(l) <= 1:
        return l[0]
    else:
        return l[0] * recursiva(l[1:])
        
        

b= [1,5,3,6,9,7]
c = [1]
r = recursiva(b)
print(r)


# Escriba una función recursiva para replicar los elementos de una lista una cantidad n de veces
#ejemplo: replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

def replicar(l:list, n) -> list:
    if len(l) < 1 or n < 1:
        return l
    else:
        return l, replicar(l,n) #corregir
    
k= replicar(b,2)
print(k)

    







