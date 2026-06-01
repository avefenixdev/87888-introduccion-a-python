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