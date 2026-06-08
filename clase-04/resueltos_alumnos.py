# Marco
notas_alumno = []

def cant_elementos(notas):
    return len(notas)

def suma_notas(notas):
    return sum(notas)

def calcular_prom(total, elementos):
    promedio = 0
    if(elementos != 0):
        promedio = total /elementos
    return promedio

def agregar_nota(notas, nota):
    notas.append(nota)

def mostrar_notas(notas):
    if(cant_elementos(notas) == 0):
        print("No se ingresaron notas")
    else:
        for i in range(cant_elementos(notas)):
            print(f"Instancia evaluativa: {i + 1} - Nota: {notas[i]} ")

def mostar_prom():
        sumatoria_notas = suma_notas(notas_alumno)
        cantidad_notas = cant_elementos(notas_alumno)
        promedio = calcular_prom(sumatoria_notas, cantidad_notas)
        if(promedio >= 4):
            print(f"Aprobado con {promedio:.2f} ")
        else:
            print(f"Desaprobado con: {promedio:.2f}")

while True:
    nota = float(input("Ingrese la nota del alumno (Ingrese -1 para salir)"))
    
    if(nota == -1):
        break
    
    if((nota >= 1) and (nota <= 10)):
        agregar_nota(notas_alumno,nota)
    else:
        print(f"La nota: {nota} que fue ingresada es invalida. Por favor intente nuevamente")

print("-------------------")
mostrar_notas(notas_alumno)
print("-------------------")
mostar_prom()

#Luciano
notas = []
def agregar_nota_lista(nota):
    notas.append(nota)

def cantidad_elementos(notas):
    cant_elementos = len(notas)
    return cant_elementos

def calcular_total_notas(notas):
    total = sum(notas)
    return total

def calcular_promedio_notas(total, cant_elementos):
    promedio = total / cant_elementos
    promedio_redondeado = round(promedio, 2)
    return promedio_redondeado

def imprimir_notas(notas):
    for nota in notas:
        print(f"Nota examen: {nota}")
        
while True:
    # 2
    nota = float(input("Ingrese la nota del examen (-1 para terminar): "))

    if nota == -1:
        break
    elif nota < 1 or nota > 10:
        print("Error: la nota debe ser un numero entre 1 y 10")
    else:
        agregar_nota_lista(nota)

if cantidad_elementos(notas) == 0:
        print("No se cargaron notas")
else:
    total = calcular_total_notas(notas)
    cant_elementos = cantidad_elementos(notas)
    promedio = calcular_promedio_notas(total, cant_elementos)
    
    if promedio >= 4:
        imprimir_notas(notas)
        print(f"Promedio: {promedio}, Aprobaste la materia!")
    else:
        imprimir_notas(notas)
        print(f"Promedio: {promedio}, Debes ir a recuperatorio.")

#Mora
def registrar_notas():
    notas = []
    while True:
        ingreso = int(input("Ingrese una nota (entre 1 y 10) o ingrese -1 para finalizar : "))

        if ingreso >= 1 and ingreso <= 10:
            notas.append(ingreso)
            continue
        elif ingreso == -1:
            break
        else:
            print("La nota debe ser positiva y estar entre 1 y 10.")

    print(f"Las notas ingresadas son: \n{notas}\n")
    return notas

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    print(f"Tu promedio es {promedio:.2f}\n")
    return promedio

def aprobacion(promedio):
    if promedio >= 4:
        print("Aprobaste\n")
    else:
        print("Recuperatorio\n")

def programita():
    notas = registrar_notas()
    promedio = calcular_promedio(notas)
    aprobacion(promedio)

programita()

# Maxi -------------

def pedir_nota():
    while True:
        try:
            nota = int(input("Ingrese su nota (Entre 1 y 10): "))
            return nota
        except ValueError:
            print("Error")
def validar_rango(nota):
    if 1 <= nota <= 10:
        return True
    return False
def hacer_validaciones(nota):
    if not validar_rango(nota):
        print("Error. Nota no esta en el rango entre 1 y 10")
        return False
    return True
def calcular_notas():
    lista_notas = []
    while True:
        nota = pedir_nota()
        if nota == -1:
            break
        elif not hacer_validaciones(nota):
            continue
        lista_notas.append(nota)
    return lista_notas
def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)
def se_aprobo_materia(promedio):
    if promedio >= 4:
        return True
    return False
def definir_resultado(resultado):
    if not resultado:
        return "Recuperar"
    return "Aprobado"
def imprimir_resultado(promedio, resultado, lista_notas):
    print("Notas: ", end="")
    print(*lista_notas, sep=" - ")
    cursada = definir_resultado(resultado)
    print(f"La materia fue para {cursada} con un promedio de {promedio}.")
def regularizar_materia():
    lista_notas = calcular_notas()
    if not lista_notas:
        return
    promedio = calcular_promedio(lista_notas)
    resultado = se_aprobo_materia(promedio)
    imprimir_resultado(promedio, resultado, lista_notas)
regularizar_materia()

# rodrigo
notas_alum = []

def cargar_notas():
    while True:
        nota = int(input("Ingrese una nota (1-10) o -1 para finalizar:  "))

        if nota == -1:
            break

        if 1 <= nota <= 10:
            notas_alum.append(nota)
        else:
            print("Error: la nota debe estar entre 1 y 10")

    return notas_alum

def mostrar_notas(notas):
    strin = " "

    for i in range(len(notas)):
        strin += str(notas[i])

        if i < len(notas) - 1:
            strin += " - "

    print(strin)

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

notas_final = cargar_notas()
promedio = calcular_promedio(notas_final)
mostrar_notas(notas_final)

print(f"El promedio es:  {promedio}")

if promedio >= 4:
        print("APROBASTe FELICIDADES ")
else:
        print("LO SIENTO TE TOCA RECUPERATORIO")

# Judith
#Judith
print("¡Bienvenido al programa!")
list_notes = []
while True:
    note = float(input("Ingrese una nota (0 para finalizar): "))
    if note == 0:
        break
    if note < 1 or note > 10:
        print("Error: Recuerdá que la nota debe estar entre 1 y 10.")
    else:
        list_notes.append(note)
if len(list_notes) == 0:
    print("No se ingresaron notas.")
else:
    total = sum(list_notes)
    average = total / len(list_notes)
    print("Las notas ingresadas son:")
    for note in list_notes:
        print(note, end=" - ")
    print() # Salto de línea para que sea más legible
    print(f"El promedio es de: {average:.2f}.")
    if average >= 4:
        print("¡Felicidades! Aprobaste, sos un crack.")
    else:
        print("¡No siempre se puede! Vas a recuperatorio, ponele buena que vos podes.")

# Arnold

# Arnold
nota = []
promedio = 0
def agregar_nota(notas):
    nota.append(notas)
def cantidad_notas(nota):
    cant_notas = len(nota)
    return cant_notas
def promedio_notas(nota, cant_notas):
    suma = sum(nota)
    promedio = suma / cant_notas
    return promedio
def mostrar_notas(nota):
    str_notas = " / ".join(str(n) for n in nota)
    print(f"Las notas son: {str_notas}")
def mostrar_promedio(promedio):
    print(f"El promedio es: {promedio:.2f}")
    if promedio > 4:
        print("Aprobaste.")
    elif promedio < 4:
        print("Reprobaste, a recuperatorio.")
while True:
    notas = float(input("Ingrese una nota (-1 para terminar): "))
    if notas == -1:
        break
    elif notas > 10:
        print("Ingrese una nota válida entre 1 y 10")
    elif notas < 1:
        print("Ingrese una nota válida entre 1 y 10")
    else:
        agregar_nota(notas)

    if cantidad_notas(nota) == 0:
        print("No se ingresaron notas")
    else:
        promedio = promedio_notas(nota, cantidad_notas(nota))
mostrar_notas(nota)
mostrar_promedio(promedio)

# Noelia
def ingreso_notas():
    lista_numeros = []
    print("Bienvenido, ingrese sus notas a continuación (-1 para terminar):")
    while True:
        try:
            numero = int(input("Ingrese una nota: "))
            if numero == -1:
                break
            if numero < -1 or numero > 10:
                print("Ingrese una nota válida (1 - 10)")
                continue
            lista_numeros.append(numero)
        except ValueError:
            print("Error: debe ingresar un número entero.")
    return lista_numeros
def mostrar_notas(lista_numeros):
    print("\nNotas ingresadas:")
    for num in lista_numeros:
        print(num)
def promedio_notas(lista_numeros):
    if not lista_numeros:
        print("No se ingresaron notas para calcular el promedio.")
    else:
        valor = sum(lista_numeros) / len(lista_numeros)
        print(f"\nPromedio: {valor:.2f}")
        if valor >= 4:
            print("Usted aprobó la materia. ¡Felicitaciones!")
        else:
            print("Usted no aprobó la materia. Deberá asistir a recuperatorio.")
notas = ingreso_notas()
mostrar_notas(notas)
promedio_notas(notas)