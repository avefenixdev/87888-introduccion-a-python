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
