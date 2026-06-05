# Maxi
def imprimir_numeros(lista_numeros):
    print(*lista_numeros, sep = ", ")
def calcular_suma(lista_numeros):
    return sum(lista_numeros)
def calcular_promedio(lista_numeros, sumatoria):
    return round(sumatoria / len(lista_numeros), 2)
def imprimir_resultado(lista_numeros, sumatoria, promedio):
    print("\n--- Resultado ---")
    imprimir_numeros(lista_numeros)
    print(f"La suma de los números dentro de la lista es: {sumatoria}")
    print(f"El promedio de los numeros dentro de la lista es: {promedio}\n")

lista_numeros = [10, 22, 55, 2, 88, 7]
sumatoria = calcular_suma(lista_numeros)
promedio = calcular_promedio(lista_numeros, sumatoria)
imprimir_resultado(lista_numeros, sumatoria, promedio)

# rocio
def calcularSuma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
def calcularPromedio(numeros):
    cantidad_elementos = len(numeros)
    return calcularSuma(numeros) / cantidad_elementos
def imprimirNumeros(numeros):
    print("Números en la lista:")
    for numero in numeros:
        print(numero)
def imprimirSumaYPromedio( suma, promedio) :
    print(f"La suma de los números dentro de la lista es: {suma}")
    print(f"El promedio de los números dentro de la lista es: {promedio}")
# Programa principal
numeros = [10, 22, 55, 2, 88, 7]
imprimirNumeros(numeros)
imprimirSumaYPromedio(calcularSuma(numeros), calcularPromedio(numeros))

# luciano
def imprimir_numeros(numeros):
    for numero in numeros:
        print(numero)
def calcular_suma(numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(f"La suma de los numeros dentro de la lista es: {total}")
def calcular_promedio(numeros):
    total = 0
    promedio = 0
    for numero in numeros:
        total += numero
    promedio = round(total/len(numeros), 2)
    print(f"El promedio de los numeros dentro de la lista es: {promedio}")
lista_uno = [10, 22, 55, 2, 88, 7]
imprimir_numeros(lista_uno)
calcular_suma(lista_uno)
calcular_promedio(lista_uno)

#Judith D
print("¡Feliz viernes! Bienvenido al programa refactorizado")
def print_numbers(list_numbers):
    print("Tus números de la suerte son: ")
    for numero in list_numbers:
        print(numero, end=", ")
    print()
def calculate_sum(list_numbers):
    return sum(list_numbers)
def calculate_average(list_numbers):
    return sum(list_numbers) / len(list_numbers)
def print_results(sum_result, average):
    print("___________________________________________________________________________")
    print(f"La suma de los números dentro de la lista es: {sum_result}")
    print(f"El promedio de los números dentro de la lista es: {average:.2f}")
    print("¡Gracias por usar nuestros servicios!")
list_numbers = [10, 22, 55, 2, 88, 7]
print_numbers(list_numbers)
sum_result = calculate_sum(list_numbers)
average = calculate_average(list_numbers)
print_results(sum_result, average)

# rodrigo
lista_num = [10, 22, 55, 2, 88, 7]

def imprimir (num):
    for i  in range(len (num)):
        print(num[i])

def sumar(num):
    solucion = 0
    for j in num:
        solucion += j
    return solucion
    
def promediar(num):
    solucion = 0
    solucion = sumar(num) / len(num)
    return solucion

print("***IMPRIMIR CADA NUMERO***")
imprimir(lista_num)

print("***CALCULAR LA SUMA***\n")
resp1 = sumar(lista_num)
print(f'La suma de los numeros dentro de la lista es: {resp1} ')

print("***CALCULAR LA PROMEDIO***\n")
resp2 = promediar(lista_num)
print(f"El promedio de los numeros dentro de la lista es: {resp2}")

# sofia
def imprimir_numeros(numeros):
    for n in numeros:
        print(n)
def sumar(numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma
def calcular_promedio(numeros):
    suma  = sumar(numeros)
    promedio = suma/len(numeros)
    return promedio

lista_numeros = [10, 22, 55, 2, 88, 7]
imprimir_numeros(lista_numeros)
resultado_suma = sumar(lista_numeros)
resultado_promedio = calcular_promedio(lista_numeros)
print(f"La suma de los números dentro de la lista es: {resultado_suma}")
print(f"El promedio de los números dentro de la lista es: {resultado_promedio}")

# Micaela
#Zona de funciones
def imprimir_numeros(lista):
    for numero in lista:
        print(numero)
def calcular_suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
def calcular_promedio(lista):
    return calcular_suma(lista) / len(lista)
# Lista 
numeros = [10, 22, 55, 2, 88, 7]
# Imprimir
imprimir_numeros(numeros)
# Calcular suma y promedio
suma = calcular_suma(numeros)
promedio = calcular_promedio(numeros)
# Mostrar resultados
print(f"La suma de los números dentro de la lista es: {suma}")
print(f"El promedio de los números dentro de la lista es: {promedio}")

# lucia
#Creamos la lista
numeros = [10, 22, 55, 2, 88, 7]

#Creamos las funciones
def calcular_suma_e_imprimir(lista_numeros):
    """ Recorre la lista, imprime cada número y devuelve la suma total. """
    print("--- Números dentro de la lista ---")
    suma_total = 0
    for numero in lista_numeros:
        print(numero)
        suma_total += numero
    print("----------------------------------")
    return suma_total

def calcular_promedio(total_suma, cantidad_elementos):
    """Calcula y devuelve el promedio."""
    return total_suma / cantidad_elementos


# Llamamos a las funciones y guardamos sus resultados en variables
suma = calcular_suma_e_imprimir(numeros)
cantidad = len(numeros)
promedio = calcular_promedio(suma, cantidad)

#Mostramos los resultados
print(f"La suma de los números dentro de la lista es: {suma}")
print(f"El promedio de los números dentro de la lista es: {promedio}")

# Mauro
listaNumeros = [10, 22, 55, 2, 88, 7]
def ImprimirLista(lista):
    print(f"Lista: {lista}")
def Suma(numeros):
    total = 0
    for i in numeros:
        total += i
    return total
def Promedio(numeros):
    return Suma(numeros) / len(numeros)
ImprimirLista(listaNumeros)
print(f"Suma: {Suma(listaNumeros)}")
print(f"Promedio: {Promedio(listaNumeros)}")

# Noelia
def imprimir_numeros(lista_numeros):
    for num in numeros:
        print(f"{num:.2f}")
def suma(lista_numeros):
    return sum(numeros)
def promedio(lista_numeros):
     return suma(lista_numeros) / len(lista_numeros)
def imprimir_en_pantalla(lista_numeros):
    print("=" * 40)
    print("              RESULTADO")
    print("=" * 40)
    print(f"Cantidad de numeros : {len(lista_numeros)}")
    print(f"Suma total          : {suma(lista_numeros):.2f}")
    print(f"Promedio            : {promedio(lista_numeros):.2f}")
numeros = [10, 22, 55, 2, 88, 7]
imprimir_en_pantalla(numeros)

# Mora
lista1 = [10, 22, 55, 2, 88, 7]

def sumarlista(lista_a_sumar):
    total = 0
    for n in lista_a_sumar:
        total += n
    return total

def longitud(lista_a_medir):
    longitud= len(lista_a_medir)
    return longitud

def promedio(lista_a_promediar):
    resultado = sumarlista(lista_a_promediar) / longitud(lista_a_promediar)
    return resultado

def imprimir_datos_lista(lista):
    print(f"La suma de los numeros dentro de la lista es: {sumarlista(lista):.2f}")
    print(f"El promedio de los números dentro de la lista es: {promedio(lista):.2f}")

imprimir_datos_lista(lista1)

# Angeles
""" Funciones """
def imprimir_numeros(numeros):
    for n in numeros:
        print(n)
def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
def calcular_promedio(suma, cantidad_elementos):
    return suma / cantidad_elementos
""" --------------------------------- """
""" Variables """
lista_numeros = [ 4, 5, 8, 11, 12, 24]
cant_elementos = len(lista_numeros)
suma = sumar_lista(lista_numeros)
promedio = calcular_promedio(sumar_lista(lista_numeros), cant_elementos)
""" --------------------------------- """
print("------------------------------------------")
print("Lista:")
imprimir_numeros(lista_numeros)
print("------------------------------------------")
print(f"La suma de los números dentro de la lista es: {suma}")
print("------------------------------------------")
print(f"El promedio de los números dentro de la lista es: {promedio}")

# Gina
def suma(numeros):
    return sum(numeros)
def promedio(numeros):
    total_suma = suma(numeros)
    cantidad = len(numeros)
    return total_suma / cantidad
def resultados(numeros):
    print("Números dentro de la lista:")
    for numero in numeros:
        print(numero)
        
    print("-" * 40)
    
    suma_total = suma(numeros)
    promedio_total = promedio(numeros)
    
    print(f"La suma de los números dentro de la lista es: {suma_total}")
    print(f"El promedio de los números dentro de la lista es: {promedio_total}")
numeros = [10, 22, 55, 2, 88, 7]
resultados(numeros)

# Luciano (Versión nueva)
def imprimir_numeros(numeros):
    for numero in numeros:
        print(numero)
def calcular_suma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
def calcular_promedio(numeros):
    total = 0
    promedio = 0
    for numero in numeros:
        total += numero
    promedio = round(total/len(numeros), 2)
    return promedio
def imprimir_resultados(numeros):
        print(f"La suma de los numeros dentro de la lista es: {calcular_suma(numeros)}")
        print(f"El promedio de los numeros dentro de la lista es: {calcular_promedio(numeros)}")
lista_uno = [10, 22, 55, 2, 88, 7]
lista_dos = [2, 45, 26, 13, 5, 70]
imprimir_numeros(lista_uno)
# calcular_suma(lista_uno)
# calcular_promedio(lista_uno)
imprimir_resultados(lista_uno)