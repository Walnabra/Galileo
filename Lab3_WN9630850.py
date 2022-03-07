#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Pregunta 1, convertir numero entero decimal a binario.

numero = int(input("Ingrese un numero entero: ")) #ingresamos el numero que vamos a representar en binario
modulos = [] # la lista para guardar los módulos
while numero != 0: # mientras el número de entrada sea diferente de cero
    # paso 1: dividimos entre 2
    modulo = numero % 2
    cociente = numero // 2
    modulos.append(modulo) # guardamos el módulo calculado
    numero = cociente # el cociente pasa a ser el número de entrada
print(modulos)


# In[21]:


# Pregunta 2, funcion que devuelva verdadero si el numero es primo.

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Ingrese un numero: '))
    result = isPrime(num)

    if result is True:
        print('El numero es primo!!')
    else:
        print('El numero no es primo!!')
if __name__ == '__main__':
    app()


# In[87]:


# Pregunta 3, SIN USAR FUNCION; Dada una lista de n numeros, calcule la desviación estandar del conjunto de numeros.

lista = [2, 3, 4, 5]
print("Lista: " +  str(lista))
mean = sum(lista) / len(lista)
print("El promedio es: " + str(mean))
#creación de formula desviación standard
a1 = (1/(len(lista) - 1))
p0 = lista[0]
p1 = lista[1]
p2 = lista[2]
p3 = lista[3]
a3 = (((p0 - mean)**2) + ((p1 - mean)**2) + ((p2 - mean)**2) + ((p3 - mean)**2))
desviacionstd = ((a1 * a3)** (0.5))
print("La desviación estandar SIN FUNCION es: " + str(desviacionstd))


# In[7]:


# Pregunta 4, con Algoritmo de ordenamiento BubbleSort, ordena el arreglo.
def bubbleSort(nums):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                intercambio = True
            
lis = [7, 3, 1, 10, 8]
bubbleSort(lis)
print("El arreglo ordenado queda asi: " + str(lis))


# In[12]:


# Pregunta 5, Dada una Tupla de numeros o letras esta se convierta en un string.

tupla = ('10', '20', '40', '5', '70')
tupla
str = ''.join(tupla)
print (str)


# In[49]:


# Pregunta 6, Dada una lista de tuplas, eliminar tuplas vacias.

lista = [(),(),('X'),('a','b'),('a','b','c'),('d')]
del lista[0]
del lista[0]
tupla1 = tuple(lista)
print(tupla1)


# In[62]:


# Pregunta 7, Dada una tupla de tuplas con numeros, devuelva una tupla individual con el promedio de cada una.

tuplas = ((10,10,10,12), (30, 45, 56, 45), (81,80, 39, 32))
tuplas1 = tuplas[0]
lista1 = list(tuplas1)
tuplas2 = tuplas[1]
lista2 = list(tuplas2)
tuplas3 = tuplas[2]
lista3 = list(tuplas3)
prom1 = (sum(lista1) / len(lista1))
prom2 = (sum(lista2) / len(lista2))
prom3 = (sum(lista3) / len(lista3))
lista_promedios = [(prom1), (prom2), (prom3)]
print(lista_promedios)


# In[ ]:




