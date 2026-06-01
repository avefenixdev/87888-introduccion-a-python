print("Condicionales (Tomar decisiones)")

edad = 21

print("Inicio programa")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    print("No puedes ingresar")
print("Fin del programa")

# En Python se trabaja identado nuestraws sentencias cuando trabajamos con bloques

print("-------------------------")
print("Bloque if sin else")

if edad >= 18:
    print("Mayor de edad")
    print("Podes votar")
print("Fin del programa")

print("---------------------------------")

print("3 caminos o más con el if else -> elif")

nota = 3.5

if nota < 4:
    print("Desaprobado")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Muy bien")
else:
    print("Excelente")

# En Python el == de los operadores de comparación es por diseño estricto.
# No estricto solo comparaba valor en javascript (==) y el estricto (===) comparaba valor y tipo 
# is -> comporando es referencia de memoria. obj1 is obj2

print("Operadores lógicos")

print("and (y lógico)")

edad = 25
tiene_licencia = True

# 1 -> TRUE | 0 -> False
# a and b = res
# 1     1 = 1 <--------------------------------------------------------- Ambas verdaderas
# 1     0 = 0
# 0     1 = 0
# 0     0 = 0
#       True    and     False 
if ( edad >= 18 and tiene_licencia):
    print("Puedes manejar")
else:
    print("No puedes manejar")


