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