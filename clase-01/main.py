print("¡Hola mundo!")

print("Comentario en una línea")

# Una sola línea
# Otra línea

print("Comentario en varias líneas")
# Shortcut comentarios multiline (Alt + Shift + A)

""" En 
Varias
Líneas """

print("Variables")

nombre = "Maxi"
print(nombre) # Cadena (String)

print(type(nombre)) # str

edad = 22
print(edad) # número

print(type(edad)) # int

is_teacher = True # snake_case -> palabra_1_palabra_2_palabra_3

print(is_teacher) # booleano

print(type(is_teacher)) # bool

is_teacher = False
print(is_teacher)

print("Concatenación de cadenas")

precio = 33.99
print(precio) # flotante
print(type(precio)) # float

# Concatenar (juntar texto -> unir textos)

segundo_nombre = "Luis"
apellido = "Principe"

nombre_completo = nombre + " " + segundo_nombre + " " + apellido
print(nombre_completo)

# f-strings (Muy parecido al template string de javascript)
# const nombreCompleto = `${nombre} ${segundo_nombre} ${apellido}`

nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
print(nombre_completo)

# join (muchas cadenas)
nombre_completo = " ".join([nombre, segundo_nombre, apellido])
print(nombre_completo)

texto = "La" * 3
print(texto) # LaLaLa

print("Función input(): Para pedir datos al usuario")

# print(input("Escriba aquí su nombre: "))
dato = input("Escriba aquí su nombre: ")
print(dato)
print(f"Hola {dato}")
print("Hola " + dato)

print("Casteo (Conversión de tipos)")

cantidad_alumnos = input("¿Cuántos alumnos están en clase? ")
print(cantidad_alumnos) # Esto es una cadena
# print(cantidad_alumnos + 2) No puedo hacer operaciones aritmeticas con cadenas
print(type(cantidad_alumnos)) # str
cantidad_alumnos = int(cantidad_alumnos) # casteo una cadena a número
print(type(cantidad_alumnos)) # int
cantidad_personas = cantidad_alumnos + 2
print(cantidad_personas)
print(type(cantidad_personas)) # int
