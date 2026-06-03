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