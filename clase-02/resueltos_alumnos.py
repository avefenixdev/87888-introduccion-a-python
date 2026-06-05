# Sasha
monto_a_calcular = float(input("Ingrese monto a calcular: "))
consulta = input ("¿Quiere conversión a dólar o euro?: ")
if consulta == "dólar" or consulta == "dolar":
    valor_dolar = 1400
    resultado = monto_a_calcular / valor_dolar
    print(f"El resultado en dólares es: {resultado}")
elif consulta == "euro":
    valor_euro = 1600
    resultado = monto_a_calcular / valor_euro
    print(f"El resultado en euros es: {resultado}")
else:
    print("Opción no válida")

# Maxi
pesos = float(input("> Ingrese el monto que desea convertir en pesos: "))
moneda = input("> Ingrese la moneda que quiere convertir\n  (Dolares/Euros): ").lower().capitalize()
print()
# valor_moneda = 150
# cantidad_convertida = pesos / valor_moneda
match moneda:
    case "Dolares":
        valor_moneda = 1400
        cantidad_convertida = pesos / valor_moneda
        print(f"> Con {pesos} pesos se puede comprar {cantidad_convertida} Dolares")
    case "Euros":
        valor_moneda = 1600
        cantidad_convertida = pesos / valor_moneda
        print(f"> Con {pesos} pesos se puede comprar {cantidad_convertida} Euros")
    case _:
        print("> Error. No se pudo procesar el cambio")

# Marco
cambio_dolar = 1427.01
cambio_euro = 1655.46
pesos_usuario = int(input("Ingrese la cantidad de que quiere cambiar: "))
print("---------------------------------------------")
print(f"tipo de cambio Dolar: {cambio_dolar} - tipo de cambio Euro: {cambio_euro}")
divisa = input("Ingrese a que divisa quiere cambiar sus pesos: ")
cantidad = 0
match divisa.lower():
    case "dolar":
        cantidad = pesos_usuario / cambio_dolar
        print(f"Con ${pesos_usuario} se pueden comprar ${cantidad:.2f} dolares")
    case "euro":
        cantidad = pesos_usuario / cambio_euro
        print(f"Con ${pesos_usuario} se pueden comprar ${cantidad:.2f} euros")
    case _:
        print("Divisa invalida, ingrese nuevamente los datos")

# Luciano

monto = float(input("Ingrese su monto a cambiar en pesos: "))
moneda = input("Seleccione la moneda por la que desea cambiar dolar/euro: ").lower()
match moneda:
    case "dolar" | "dolares":
        cambio = round(monto / 1426.98, 2)
        print(f"Con {monto} pesos se compran {cambio} dolares")
    case "euro" | "euros":
        cambio = round(monto / 1655.43, 2)
        print(f"Con {monto} pesos se compran {cambio} euros")
    case _:
        print("La opcion ingresada no es correcta, indique la moneda en dolar o euro")

# Judith
print("¡Bienvenido a nuestra máquina cambio de divisas!");
amount_money = float(input("Ingrese la cantidad de pesos a convertir, porfavor: "))
currency = input("¿Desea convertir a dolares o euros? ")
"""
Dolar según 'Dolar hoy': $1415
Euros según 'Dolarito': $1705,74
Busco un punto medio
"""
match currency:
    case "dolares":
        result = amount_money / 1400;
        print(f"Con ${amount_money} pesos se compran {result} dolares");
    case "euros":
        result = amount_money / 1700;
        print(f"Con {amount_money} pesos se compran {result} euros");
    case _:
        print(f"{amount_money} no es un monto válido, intente nuevamente");

# Angeles
print("Ejercicio 2")
print("------------------------------------------")
print("¡Hola! En el siguiente programa te ayudaré a convertir tus pesos argentinos a dólares o euros.\n")

pesos_usuario = int(input("Indicanos la cantidad de pesos argentinos que desea convertir: "))

if pesos_usuario > 0:
    moneda_deseada = input("¿A qué modena desea convertir, dolares o euros? ")
    match moneda_deseada:
        case "dolares":
            dolares = pesos_usuario / 1420
            print(f"\nCon {pesos_usuario} pesos se compra {dolares} dolares")
        case "euros":
            euros = pesos_usuario / 1650
            print(f"\nCon {pesos_usuario} pesos se compra {euros} euros")
        case _:
            print("No puedo hacer esa conversion")
else:
    print("Ese no es un valor válido.")

# Rocio
dolar = 1500
euro = 1655
pesos = input("Ingresa la cantidad de pesos argentinos: ")
print("A que moneda deseas convertir?")
print("1. Dolares")
print("2. Euros")
opcion = input("Selecciona una opcion: ")
if opcion == "1":
    dolares = float(pesos) / dolar
    print(f"Con {pesos} pesos se compran {int(dolares)} dolares")
elif opcion == "2":
    euros = float(pesos) / euro
    print(f"Con {pesos} pesos se compran {int(euros)} euros")
else:
    print("Opcion no valida")

# Leonardo
pesos = float(input("Ingresse una cantidad de pesos argentinos: "))
moneda = input("ingrese la moneda (dolares o euros): ")
if moneda == "dolares":
    dolares = pesos / 150
    print("Con", pesos, "pesos se pueden comprar", dolares, "dolares")
elif moneda == "euros":
    euros = pesos / 170
    print("Con", pesos, "pesos se pueden comprar", euros, "euros")
else:
    print("Moneda no valida")

# Romina
precio_dolar= 1430
precio_euro= 1660
cantidad_float= input("Ingrese cantidad de pesos Argentinos:")
moneda= input("¿A que moneda convertir?(DOLAR/EURO):")
cantidad= float(cantidad_float)
if moneda== "dolar":
    resultado = cantidad / precio_dolar
    print("Con" + cantidad_float + "pesos podes comprar" + resultado + "dolares")
elif moneda == "euro":
    resultado = cantidad / precio_euro
    print("Con" + cantidad_float + "pesos podes comprar" + resultado + "euros")
else:
    print("Moneda no reconocida. Ingrese DOLAR O EURO")

# Gregorio
dolar = 1500
euro = 1700
pesos = float(input("Ingrese cantidad pesos ARS: "))
moneda = input("seleccionar moneda? (dolar/euro): ").lower()
match moneda:
    case "dolar":
        resultado = pesos / dolar
        print(f"Con {pesos} pesos se pueden comprar {resultado:.2f} dolares")
    case "euro":
        resultado = pesos / euro
        print(f"Con {pesos} pesos se pueden comprar {resultado:.2f} euros")
    case _:
        print("Moneda no válida")
    
# Lucia
# 1. Pide los datos al usuario
pesos = float(input("Ingrese la cantidad de pesos argentinos: "))

print("¿A qué moneda desea convertir?")
print("1 - Dólares")
print("2 - Euros")
opcion = input("Seleccione una opción (1 o 2): ")

precio_dolar = 1400
precio_euro = 1680

# 2 y 3. Evalua con match y muestra el resultado
match opcion:
    case "dolares" | "dolar" | "1":
        resultado = pesos / precio_dolar
        print(f"Con {pesos} pesos se compran {resultado:.2f} dolares")
    case "euros" | "euro" | "2":
        resultado = pesos / precio_euro
        print(f"Con {pesos} pesos se compran {resultado:.2f} euros")
    case _: 
        print("Moneda no reconocida. Intente con 'dolares' o 'euros'.")

# Mora
print("Bienvenido al programa de cambio de divisas")
precioeuro = 1700
preciodolar = 1400

pesos = int(input("Ingrese cantidad de $ (pesos argentinos) en números: \n"))
print(f"Usted ha ingresado ${pesos} pesos argentinos")
verificacion = str(input("¿El monto es correcto? Ingrese si o no: \n"))
if (verificacion == "si"):
    cambiara = str(input("¿Desea cambiar sus $ argentinos a euros o dolares?"))

if (cambiara == "euros"):
    montoeuros=pesos/precioeuro
    print(f"Su monto en euros es: ${montoeuros}.")

if (cambiara == "dolares"):
    montodolar=pesos/preciodolar
    print(f"Su monto en dolares es: ${montodolar}.")

# Sofia
print("Buenos dias!")
opcion = int(input("Seleccione la modena a cambiar: \n1. Dolares \n2. Euros"))
monto_cambiar = float(input("Ingrese el monto a cambiar: $"))
match opcion:
    case 1: 
        dolar = monto_cambiar
        dolar = dolar / 15000
        print(f"Con {monto_cambiar} pesos se puede comprar {dolar} dolar")
        
    case 2:
        euro = monto_cambiar
        euro = euro / 15000
        print(f"Con {monto_cambiar} pesos se puede comprar {euro} euros")
    case _:
        print("Dato erroneo")

# Rodrigo
print("-----------CONVERSOR DE DIVISAS-----------\n------------------------------------------")
# Variables
euros = 0
dolar = 0
cotizacion_venta_euros = 1655,28
cotizacion_venta_dolares = 1426,98
pesos = input("INGRESE SU MONTO EN PESOS ($):   ")
pesos = int(pesos)

print("---------------------------------------------")
control = input("INGRESE 1 para convertir a EUROS \nNGRESE 2 para convertir a DOLARES:  ")

print("---------------------------------------------")
match control:

    case "1":
        euros = pesos / cotizacion_venta_euros
        print(f"Usted puede comprar con: {pesos} PESOS a {euros} EUROS  \nDato extraido del conversor oficial de GOOGLE")
    case "2":
        dolar = pesos / cotizacion_venta_dolares
        print(f"Usted puede comprar con: {pesos} PESOS a {dolar} EUROS \nDato extraido del conversor oficial de GOOGLE")
    case _ :
        print(" POR FAVOR INGRESE UNA OPCION VALIDA")
print("---------------------------------------------")

# Agustin
tasa_cambio_dolar = 7.0e-4 
tasa_cambio_euro = 6.0e-4 
cantidad_pesos = float(input("Ingrese la cantidad de pesos Argentinos: "))
moneda_destino = input("Ingrese la moneda a la que desea convertir (dolar/euro): ").lower()
if moneda_destino == "dolar":
    cantidad_convertida = cantidad_pesos * tasa_cambio_dolar
    print(f"{cantidad_pesos} pesos Argentinos equivalen a {cantidad_convertida:.2f} dólares.")
elif moneda_destino == "euro":
    cantidad_convertida = cantidad_pesos * tasa_cambio_euro
    print(f"{cantidad_pesos} pesos Argentinos equivalen a {cantidad_convertida:.2f} euros.")
else:
    print("Moneda no válida. Por favor, ingrese 'dolar' o 'euro'.")

# Arnold
Dolar = 1426.99
Euro = 1655.43
Monto = float(input("Ingrese monto (En pesos argentinos): "))
Tipo_de_cambio = input("Indique tipo de cambio (Dólares/Euros): ").lower()
match Tipo_de_cambio:
    case "dolares":
        Monto_final = Monto / Dolar
        print(f"Con {Monto} pesos se pueden comprar {Monto_final:.2f} dolares")
    case "euros":
        Monto_final = Monto / Euro
        print(f"Con {Monto} pesos se pueden comprar {Monto_final:.2f} euros")
    case _:
        print("Tipo de cambio inválido")

# -----------------------------------------------
# -----------------------------------------------
# -----------------------------------------------

# Thiago
numeros = [10, 22, 55, 2, 88, 7]
suma = 0
promedio = 0
print('Recorrido de lista')
for valor in numeros:
    print(valor)
    suma = suma + valor
promedio = round(suma/(len(numeros)), 2)
print(f'\nLa suma de los números dentro de la lista es: {suma} \n')
print(f'El promedio de los números dentro de la lista es: {promedio} \n')

# Sasha
numeros = [ 1, 2, 3, 4, 5, 6 ]
print("Números de la lista: ")
for numero in numeros:
    print(numero)
suma = sum(numeros)
promedio = suma / len(numeros)
print(f"La suma de los números dentro de la lista es {suma}")
print(f"El promedio de los números dentro de la lista es {promedio}")

# Maxi
lista_numeros = [10,22,55,2,88,7]
suma = 0
print("----Resultado----")
print("\nNumeros: ", end = "")
for numero in lista_numeros:
    print(numero, end = " ")
    suma += numero
promedio = suma / len(lista_numeros)
print(f"\n\nLa suma de los números dentro de la lista es: {suma}")
print(f"\nEl promedio de los numeros dentro de la lista es: {promedio:.2f}\n")

# Angeles
print("Ejercicio 3 - Listas")
print("------------------------------------------")
total_suma = 0
promedio = 0
lista_numeros = [ 4, 5, 8, 11, 12, 24]
print("Lista:")
for numero in range(len(lista_numeros)):
    print(lista_numeros[numero])
print("------------------------------------------")
for numero in range(len(lista_numeros)):
    total_suma = total_suma + lista_numeros[numero]
print(f"La suma de los números dentro de la lista es: {total_suma}")
print("------------------------------------------")
promedio = total_suma / len(lista_numeros)
print(f"El promedio de los números dentro de la lista es: {promedio}")

# Romina
numeros = [10, 22, 55, 2, 88, 7]
suma=0
for i in numeros:
    print(i)
    suma=suma+i
promedio = suma/len(numeros)
print("SUMA: ", suma)
print("PROMEDIO: ", promedio)

# Arnold
numero_1 = float(input("Ingrese un número: "))
numero_2 = float(input("Ingrese otro número: "))
numero_3 = float(input("Ingrese otro número: "))
numero_4 = float(input("Ingrese otro número: "))
numero_5 = float(input("Ingrese otro número: "))
numero_6 = float(input("Ingrese otro número: "))
numeros = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6]
print(numeros)
suma = sum(numeros)
promedio = suma / len(numeros)
print(f"La suma de los números dentro de la lista es: {suma:.2f}")
print(f"El promedio de los números dentro de la lista es: {promedio:.2f}")

# Carla
numeros = [10, 22, 55, 2, 88, 7]
def imprimir (numeros):
    return numeros

def suma (numeros):
    suma = 0
    for num in numeros:
        suma = suma + num
    return suma

def promedio (numeros):
    resultado = 0
    prom = suma(numeros) / len(numeros)
    resultado = prom
    return resultado

print("la suma de los numeros de la lista es:", suma(numeros))
print("los numeros de la lista son: ", imprimir(numeros))
print("el promedio de numeros dentro de la lista es: ", promedio(numeros))

# Gregorio
suma = 0 #gregorio
lista_numeros = [44, 12, 0, 69, 2, 61, 84, 100, 122, 39, 90]
for numero in lista_numeros: #for recorro lista
    print(numero)
    suma += numero #acumulador +=
promedio = suma / len(lista_numeros)
#len = cuentador
print(f"La suma de los números dentro de la lista es: {suma}")
print(f"El promedio de los números dentro de la lista es: {promedio}")

# Mora -------------------------------------------------
lista_numeros = [2, 4, 6, 8, 10, 11]
i = 0
longitud = len(lista_numeros)
sumatotal = 0
string_numeros = ""

for numero in lista_numeros:
    string_numeros = string_numeros + f'{numero} '

print(f'Los numeros de la lista son: {string_numeros}')

while i < longitud:
    sumatotal= lista_numeros[i]+sumatotal
    i= i+1

promedio=sumatotal/longitud

print(f"La suma total de todos los números es: {sumatotal}.")
print(f"El promedio de los números dentro de la lista es: {promedio:.2f}.")

# TODO REVISAR LA CLASE QUE VIENE
# Rocio 
numeros = [10, 22, 55, 2, 88, 7]
suma=0
print("Numeros en la lista:")
for numero in numeros:
    print(numero)
    suma += numero
cantidad_elementos = len(numeros)
promedio = suma / cantidad_elementos
print(f"La suma de los números dentro de la lista es: {suma}")
print(f"El promedio de los números dentro de la lista es: {promedio}")

# Nancy
numeros = []
suma = 0
cantidad = int(input("¿Cuántos números desea ingresar? "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print("La lista es:", numeros)

for i in numeros:
    suma = suma + i

promedio = suma / len(numeros)

print(f"La suma de los números dentro de la lista es: {suma} ")

print(f"El promedio de los números dentro de la lista es: {promedio}")

# Luciano
numeros = [10, 22, 55, 2, 88, 7]
total = 0
print("Imprimir cada numero:")
for numero in numeros:
    print(numero)
print("-----------------")
for numero in numeros:
    total += numero
print(f"La suma de los numeros dentro de la lista es: {total}")
print("-----------------")
for numero in numeros:
    total += numero
    promedio = round(total/len(numeros), 2)
print(f"El promedio de los numeros dentro de la lista es: {promedio}")

# Daiana
lista = [10, 22, 55, 2, 88, 7]
for numero in lista:
    print (numero, end=", ")

suma = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5])
promedio = suma / len(lista)
print(f"La suma de los números dentro de la lista es: ", suma)
print (f"El promedio de los números dentro de la lista es: ", promedio)

# Judith
print("¡Tanto tiempo! Bienvenido al programa")
list_numbers = [10, 22, 55, 2, 88 , 7]
sum_result = 0 #Variable para guardar la suma total
print("Tus números de la suerte son: ")
for i in range(len(list_numbers)):
    sum_result += list_numbers[i] #Sumo todos los valores de la lista
    print(list_numbers[i]) #Muestro cada valor de la lista
average = sum_result / len(list_numbers)
print("__________________________________________________________")
print(f"La suma de los números dentro de la lista es: {sum_result}")
print(f"El promedio de los números dentro de la lista es: {average:.2f}")

# Edson
numeros = [10, 22, 55, 2, 88, 7]
print("Bienvenido al programa de suma y promedio")
print("Los valores iniciales son:")
for i in range(len(numeros)):
    print(numeros[i])
print("------------------------")
print("A continuación calcularemos la suma de los números")
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]
print("La suma fue calculada correctamente")
promedio = suma / len(numeros)
print("------------------------")
print("Resultados finales")
print("La suma de los números dentro de la lista es:", suma)
print("El promedio de los números dentro de la lista es:", promedio)