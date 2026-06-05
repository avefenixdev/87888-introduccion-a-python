print("Clase 03 - Introducción a Python")

print("Funciones")
""" 
Una función es un forma de guardar instrucciones con un nombre para poder reutilizarla y modificarla 
"""

# ! Problema que solucionan las funciones
""" print("Buen día Juan")
print("Buen día Ana")
print("Buen día Pedro")
print("Bun día Roberto") """

# ! Arquitectura de una función

def saludar(persona_a_saludar):
    print(f"Buen día {persona_a_saludar}")


saludar("Maxi")
saludar("Mauro")
saludar("Judith")
saludar("Lucia")
saludar("Arnold")
saludar("Martín")
saludar("Rocío")


def sumar(a, b):
    print(a + b)

sumar(2, 5)
sumar(4, 8)
sumar(1, 4)
sumar(3, 5)

# ! Funciones que retonar un número para poder reutilizarlo

""" 

Crear una función: 
    - reciba una lista de números
    - devuelva la suma
    - luego imprimir el resultado

"""

def sumar_lista(numeros):
    total = 0
    for n in numeros:
        print(n)
        total += n
    return total

lista_uno = [254, 23, 2, 5, 4, 45]
lista_dos = [32, 123, 42, 25 , 34, 15]

print("----------------------------------")
resultado_uno = sumar_lista(lista_uno)
print(f"El total de la lista uno es: {resultado_uno}")
print("----------------------------------")
resultado_dos = sumar_lista(lista_dos)
print(f"El total de la lista dos es: {resultado_dos}" )

""" 
Enunciado:
----------
Una persona anota los gastos del día en una lista de números

Se pide:
    - Guardar los gastos en una lista
    - Calcular el gasto total
    - Calcular el gasto promedio 
    - Mostrar ambos valores por pantalla
 """

# MVC
gastos = [1200, 650, 850, 450] # Modelos

# Controlador
total = sum(gastos)
cant_elementos = len(gastos)
promedio = total / cant_elementos

# Vista
print("Gasto total:", total)
print("Gasto promedio:", promedio)

""" 
Enunciado:
----------
Una persona anota los gastos del día en una lista de números

Se debe:
    - verificar que la lista no esté vacía
    - Verificar que no haya valores negativos
    - Calcular el gasto total si los datos son válidos
    - Calcular el gasto promedio si los datos son válidos
    - Mostrar ambos valores por pantalla
"""

gastos = [1200, 650, 850, 450]
cant_elementos = len(gastos)
val_minimo = min(gastos)

if cant_elementos == 0:
    print("No hay gastos cargados")
elif val_minimo < 0:
    print("Error: hay gastos negativos.")
else: 
    total = sum(gastos)
    promedio = total / cant_elementos
    print("Gasto total:", total)
    print("Gastos promedio:", promedio)
