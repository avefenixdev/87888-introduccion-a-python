print("Clase 02 - Repaso condicionales")
""" Un condicional es una estructura de control que nos permite tomar decisiones y ejecutar un código u otro dependiento el resultado de la evaluación """

voy_al_cine_scary_movie = False

if voy_al_cine_scary_movie:
    print("Fui al cine a ver la peli!")
else:
    print("No fui a verla aún!")

saldo = 1000
monto = 700

if (monto <= saldo):
    saldo = saldo - monto
    print(f"El saldo actual es: {saldo}")
    print("Pago realizado")
else: 
    print("Fondos insuficientes")

print("--------------------------------")

rol = "admin"

if rol == "admin":
    print("Acceso total")
elif rol == "editor":
    print("Acceso limitado")
else: 
    print("Acceso básico")

print('--------------------------------')

print('Estructura de control match')
""" Voy a usar match cuando lo que tengo que evaluar son datos conocidos. Opciones, roles, día de la semana """

rol_match = "editor"

match rol_match:
    case "admin":
        print("Acceso total")
    case "editor":
        print("Acceso limitado")
    case _:
        print("Acceso básico")

print('--------------------------------')

dia_semana = "osvaldo"

match dia_semana:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print(f"{dia_semana} es un día de semana")
    case "sabado" | "domingo":
        print(f"{dia_semana} es un día fin de semana")
    case _:
        print(f"{dia_semana} no es un día de la semana válido")

print('--------------------------------')

# ! Listas (Mutables)
## Las listas nos permite almacenar varios valores. Son indexadas (Arreglo... array... vector )
## - Y que se puedan modificar
## - Agregar nuevos elementos
## - Reordenar
## (alumnos, producto de carrito)
## Lista alumnos, lista de los productos dentro del carrito.

""" 
nombre = "Pedro"
nombre2 = "Carlos"
nombre3 = "Ana"
 """

nombres = ["Pedro", "Carlos", "Ana"]

## Listas homogeneas (Recomendables) -> Mismo tipo de dato
## Lista de números
numeros = [ 10, 20, 30, 40 ]
## Lista de cadenas
##            0          1         2
frutas = ["manzana", "banana", "naranja"]

## Listas heterogeneas ()
## Lista mixta
##        0     1      2      3
datos = [ 25, "Maxi", 1.70, True ]

## Lista vacía
lista_vacia = []
print(lista_vacia)
# Quiero imprimir la cadena 'manzana' por la consola'
#             0          1         2
frutas = ["manzana", "banana", "naranja"]

print(frutas[0]) # manzana
print(frutas[2]) # naraja


frutas[1] = "sandia"
print(frutas[1]) # sandia
print(frutas)
print(len(frutas))
print("Último elemento de la lista")
print(frutas[-1])
print(frutas[len(frutas)-1])

print("------------------------------------")

animales = ["tigre", "buho", "gato", "caballo", "vizcacha", "serpiente", "perro"]

print(animales)
print(len(animales))

animales[4] = 'tortuga'
print(animales)

print("Recorro la lista")
#   0               7
for i in range(len(animales)): 
    print(i, animales[i])

# Matrices
#            0       1
matriz = [[1, 2], [3, 4]]
#          0  1    0  1

print(matriz)
print("# Accedo al valor '3'")
print(matriz[1]) # [3, 4]
print(matriz[1][0]) # 3
print("# Modifico el valor 2 por 22")

matriz[0][1] = 22
print(matriz)

# matriz = [[1, 2], [3, 4]]
print("-------------------------")
# matriz = 
#   ⬇️ ⬇️ <---- columnas
#  [[1, 22], <--- fila
#   [3, 4]] <--- fila

# Recorriendo filas
for fila in matriz: 
    print(fila)

print("-------------------------")
# Recorriendo filas y valores de esas filas (columnas)
for fila in matriz:
    for valor in fila: 
        print(valor)