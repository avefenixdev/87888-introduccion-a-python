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
print("-" * 50)
print("-" * 50)

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

print("-" * 50)
print("-" * 50)

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

gastos = []
cant_elementos = len(gastos)
# val_minimo = min(gastos)

if cant_elementos == 0:
    print("No hay gastos cargados")
elif min(gastos) < 0:
    print("Error: hay gastos negativos.")
else: 
    total = sum(gastos)
    promedio = total / cant_elementos
    print("Gasto total:", total)
    print("Gastos promedio:", promedio)

print('-' * 50)
print('-' * 50)

""" 
El usuario debe ingresar gastos uno por uno
El ingreso termina cuando escribe 0

El programa debe:
    - Repetir el pedido mientras el gasto sea válido
    - No aceptar números negativos
    - Calcular total y promedio
"""

""" print('Inicio')
while True:
    gasto = float(input("Ingreso un gasto (0 para terminar):"))

    if gasto == 0:
        print('Entró al break')
        break # me saca del ciclo

    if gasto == 200:
        print('Entró al continue')
        continue # me saca de la iteración actual

    print('Siguiente iteración')

print('Fin') """

""" gastos = []

while True:
    gasto = float(input("Ingreso un gasto (0 para terminar):"))

    if gasto == 0:
        break # me saca del ciclo
    elif gasto < 0:
        print('Error: El gasto no puede ser negativo.')
    else:
        gastos.append(gasto) # | -> def agregar_gasto_lista(gasto): void
    
    if len(gastos) == 0:
        print('No se cargaron gastos.')
    else:
        # | -> def cantidad_elementos(gastos): cant_elementos
        total = sum(gastos) # | -> def calcular_total_gastos(gastos): total
        promedio = total / len(gastos) # | def calcular_promedio_gastos(total, cant_elementos): promedio
        print("Gasto total:", total) # | def mostrar_total: void
        print("Gasto promedio:", promedio) # def mostrar_promedio: void  """

print("*" * 50)
print("*" * 50)

gastos = []
total = 0
promedio = 0

def agregar_gasto_lista(gasto):
    gastos.append(gasto)

def cantidad_elementos(gastos): 
    cant_elementos = len(gastos)
    return cant_elementos
    
def calcular_total_gastos(gastos): 
    total = sum(gastos)
    return total

def calcular_promedio_gastos(total, cant_elementos):
    promedio = total / cant_elementos
    return promedio

def mostrar_total(total): 
    print("Gasto total:", total)

def mostrar_promedio(promedio):
    print("Gasto promedio:", promedio)

while True:
    gasto = float(input("Ingreso un gasto (0 para terminar):"))

    if gasto == 0:
        break # me saca del ciclo
    elif gasto < 0:
        print('Error: El gasto no puede ser negativo.')
    else:
        agregar_gasto_lista(gasto) 
    
    if cantidad_elementos(gastos) == 0:
        print('No se cargaron gastos.')
    else:
        total = calcular_total_gastos(gastos) 
        cant_elementos = cantidad_elementos(gastos)
        promedio = calcular_promedio_gastos(total, cant_elementos)
        
mostrar_total(total)
mostrar_promedio(promedio)
