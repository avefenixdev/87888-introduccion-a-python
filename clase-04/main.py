
from utils import cantidad_elementos, calcular_total_gastos, calcular_promedio_gastos, mostrar_total, mostrar_promedio
from input_utils import pedir_gasto

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
