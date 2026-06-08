print("Clase 04 - Introducción a Python")


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
