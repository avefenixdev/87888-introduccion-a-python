
from utils import cantidad_elementos, calcular_total_gastos, calcular_promedio_gastos, mostrar_total, mostrar_promedio
from input_utils import pedir_gasto

""" 
¿Qué son los módulos en Python?
    * Nos permiten organizar/ordenar el código
    * Nos permiten dividir el código en diferentes archivos (para no escribir toda lógica en un solo archivo)
    * Reutilizar código sin copiar pegar.
    * módulos dentro de python -> datetime, random, math, os, sys
 """

print("Clase 04 - Introducción a Python")

gastos = []
total = 0
promedio = 0
gasto = None

def agregar_gasto_lista(gasto):
    gastos.append(gasto)

while gasto != 0:
    # 0
    gasto = pedir_gasto()

    if gasto != 0:
        agregar_gasto_lista(gasto) 


if not gastos:
    print('No se cargaron gastos.')        
else:
    total = calcular_total_gastos(gastos) 
    cant_elementos = cantidad_elementos(gastos)
    promedio = calcular_promedio_gastos(total, cant_elementos)
        
mostrar_total(total)
mostrar_promedio(promedio)

## ! Gestión de errores
# * Erroes de sintaxis
## El programa no arranca con estos errores

""" if True
print("Hola") """

## Errores en tiempo de ejecución
# El código arranca... me permite ejecutarlo pero explota.

""" print(10 / 0) """

## Errores lógicos
# Este error depende de nosotros. Bugs

""" precio = 100
descuento = 20
total = precio - descuento / 100 """

# ? Gestión de errores con try / except

""" print("Inicio del programa")
try:
    # Todo lo que quiero que se ejecute va dentro del try
    print("Vamos a hacer la división")
    print("Pidiendo datos")
    resultado = 10 / 0
    print("Muestro resultado")
    print(resultado)
    print("Terminado")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
print("Fin del programa") """

""" print("Inicio del programa")
try:
    numero = int(input("Ingrese un número:"))
    print(10 / numero)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Ingresó un valor inválido")
print("Fin del programa") """

""" print("Inicio del programa")
try:
    numero = int(input("Ingrese un número:"))
    print(10 / numero)
except:
    print("No es correcto lo que ingresaste...")
print("Fin del programa")
 """

# ! else y finally
# * else: Lo que está en el cuerpo del else se ejecuta si el bloque try, está bien y no falla

""" try:
    x = int("a") # si sale todo bien
    print(x)
except ValueError:
    print("Error")
else: 
    print('Se pudo castear ese "5" a un entero:', x) """

# * finally: No importa lo que ocurra en el try, siempre se va a ejecutar el finally

try:
    print(10 / 2)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta sin importar si hay excepción o no. Siempre")

# Cerrar archivos
# Cerrar conexiones de base de datos
# Liberar recursos
# Logs

""" try:
    print("Abro el archivo")
    print("Leo el archivo")
    print("Escribo sobre el archivo")
except:
    print("Se quedo sin espacio en disco")
finally:
    print("Cerrando archivo") """

# ! Errores personalizados
# Es un error que creamos nosotros los programadores, un nombre claro, para un tarea especifica

# Errores genericos -> ValueError -> generico
# Errores personalizados -> EdadInvalidaError

# EdadInvalidaError.py
# ? IMPORATANTE: Todas los errores herendan de Exception
class EdadInvalidaError(Exception):
    pass

# raise -> Palabra reservada del lenguaje para lanzar una excepción
# validar_edad.py
