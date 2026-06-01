# Thiago

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
altura = float(input('Introduzca su altura: '))
es_estudiante = input('Sos estudiante? Si | No: ')
print(f'{nombre} {apellido} mide {altura}m. ¿Es estudiante?: {es_estudiante}')

# Luciano

print("Ejercicio Uno")
nombre = input("Ingre su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = input("Ingrese su altura(mentros): ")
estudiante = input("¿Es estudiante?(verdadero o falso) ")
dato_completo = f"Nombre completo: {nombre} {apellido}, altura: {altura}, estudiante: {estudiante} "
print(dato_completo)

# Gregorio

print("ejercicio uno") 
nombre = input("ingresar nombre: ")
apellido = input("ingresar apellido: ")
altura = float(input("ingresar alturaa: "))
estudiante = True
print("-----Datos Personales-----")
print(nombre)
print(apellido)
print(altura)
print(estudiante)
print("--------------------------")

# Maximiliano

nombre = input("> Ingrese su nombre: ")
apellido = input("> Ingrese su apellido: ")
altura = float(input("> Ingrese su altura en metros: "))
estudiante = input("> ¿Eres estudiante? (s/n): ")
es_estudiante = False
if estudiante == "s":
    es_estudiante = True
print()
print(f"- Datos -\nNombre Completo: {nombre} {apellido}\nAltura: {altura}\nEstudiante: {es_estudiante}\n")

# Martín

nombre = input("Ingresa tu nombre ")
apellido = input("Ingresa tu apellido ")
altura_metros = input("Cual es tu altura? ")
es_estudiante = True
# Convierto el str de altura_metros con float() para que pueda ingresar decimales
altura_metros = float(altura_metros)
# print(type(altura_metros))
print(nombre)
print(apellido)
print(altura_metros)
datos_persona = f"{nombre} {apellido}"
print(datos_persona)
# Imprimo el nombre completo y le concateno la altura usando un f-strings para que lo convierta nuevamente en texto al tratarse de un numero decimal para que salga en el mensaje
print(f"{datos_persona} tu altura  es {altura_metros}")
print(f"¿Es estudiante?: {es_estudiante}")

# Arnold

nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
altura = input("¿Cuánto medís? (Escribelo en decimales): ")
# altura = int(altura)
respuesta = input("¿Sos estudiante? (si/no): ").lower()
usuario = (f"Nombre:{nombre}, Apellido:{apellido}, Altura:{altura}, Es estudiante:{'Sí' if respuesta == 'si' else 'No'}")
print(usuario)

# Camila

print("Ejecicio Uno")
print("Ingrese sus datos ")
nombre=input("ingrese su nombre: ");
apellido=input("ingrese su apellido: ");
altura=input("ingrese su altura en metros: ");
esEstudiante=input("Es estudiante ? (S/N): ");
if(esEstudiante=="S" or esEstudiante=="s"):
   esEstudiante= True
else:
    esEstudiante=False


print("Sus datos son :")  
print(F"Nombre:{nombre} {apellido}\nAltura:{altura}\nEstudiante: {esEstudiante}" )

# Romina

nombre = "romina"
apellido= "castro"
altura= 1.63
is_estudiante= True
nombre_completo= f"{nombre} {apellido}"
print ("Mi nombre y apellido es:",nombre_completo)
print ("Altura:",altura)
print ("Estudiante:",is_estudiante)

# Sofia

print("Ejercicio Uno")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = input("Ingresar su altura: ")
is_estudiante = input("¿Es estudiante? : 1.si 2.no")
if is_estudiante == "1":
    is_estudiante = True
else:
    is_estudiante = False
altura = float(altura)
info_completa = f"Nombre: {nombre} Apellido: {apellido} Altura: {altura} Estudiante: {is_estudiante}"
print(info_completa)

# Rodrigo

var1 = input("-Ingrese su Nombre: ")
var2 = input("-Ingrese su Apellido: ")
var3 = input("-Ingrese su Altura: ")
print("-Si es estudiante presione: 1 sino ingrese: 0")
var4 = input("Ingrese si es estudiante: ")
var4 = int(var4)

print("Nombre: " + var1)
print("Apellido: " + var2)
print("Altura: " + var3)
if(var4 == 1):
    print("Es Estudiante: ")
else:
    print("No estudiante: ")

# rocio Ale

nombre_apellido = input("Ingrese nombre y apellido: ")
edad = input("Ingrese edad: ")
altura = input("Ingrese altura: ")
estudiante = input("¿Es estudiante? (si/no): ")
if estudiante.lower() == "si":
    estudiante = True
else:
    estudiante = False
print(f"Nombre y Apellido: {nombre_apellido}, edad: {edad}, altura: {altura}, estudiante: {estudiante}")

# judith

print("¡Hola! Ingrese sus datos, porfavor");
name = input("Ingrese su nombre: ");
lastname = input("Ingrese su apellido: ");
height = float(input("Ingrese su altura en metros: "));
is_student = input("¿Es estudiante? (True/False): ");
print("Sus datos ingresados son:");
print(f"Gracias {name} {lastname} por sumarse a nuestro programa.");
print(f"Su altura es de {height} metros.");
print(f"Según su respuesta, la afirmación 'Usted estudia' es: {is_student}.");

# daiana

nombre = "Daiana"
apellido = "Basualdo"
altura = 1.65
estudiante = True
print("Nombre:", nombre, ", Apellido:", apellido, ", Altura:", altura, "m, Estudiante:", estudiante )

# Rocio Dani

print("Ejercicio Uno")
print("-- Ingresar datos del usuario --")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura en metros: "))
es_estudiante = input("¿Eres estudiante? (si/no): ").lower()
print("-- Datos ingresados --")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Altura: {altura} metros")
match es_estudiante:
  case "si":
    es_estudiante = True
  case "no":
    es_estudiante = False
  case _:
    print("Valor no reconocido, se asumirá que no sos un estudiante.")
    es_estudiante = False
print(f"Es estudiante: {es_estudiante}")

# Edson 

print("Ejercicio uno") #Edson
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
nombre_completo = f"{nombre} {apellido}"
print(f"Hola {nombre_completo} mucho gusto" )
altura = float(input("Ingrese altura: "))
print("Su altura es: " , altura)
is_estudiante =input("¿Usted Es estudiante? (Si/No): ")
if is_estudiante == "Si":
    is_estudiante = True
    print("Perfecto, exitos en el estudio.")
else: 
    is_estudiante = False
    print("Perfecto, gracias por su tiempo.")

# Micaela

nombre =input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
altura_en_metros=float(input("ingrese su altura en metros: "))
es_estudiante=input("¿es un estudiante? si / no ").lower()=="si"
print(f"Nombre: {nombre} \nApellido: {apellido} \nAltura: {altura_en_metros} \nEs estudiante: {es_estudiante}")

# Angeles

print('Ejercicio 1')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
altura = input('Ingrese su altura en metros: ')
altura = float(altura)

es_alumno = input('¿Es alumno? Ingrese "True" para sí o no escriba nada (Enter) para no: ')
es_alumno = bool(es_alumno) # revisar

print(f'Nombre: {nombre} tipo: {type(nombre)}\nApellido: {apellido} tipo: {type(apellido)}\nAltura: {altura} tipo: {type(altura)}\nEs alumno: {es_alumno} tipo: {type(es_alumno)}')

# Gina

nombre = input(" ingresé el nombre : ") 
apellido = input(" ingresé el apellido : ")
altura = float(input(" ingresé la altura (en metros) : ")) # flotante

print(nombre + " " + apellido + " " + altura)

# Sasha

nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
altura = input("Ingrese su altura en metros. Ej: (1.55)m ");
altura = float(altura)
estudiante = True;
print("Tus datos son:")
# print(nombre + " " + apellido + " " + altura)
print(f"{nombre} {apellido} ${altura}")