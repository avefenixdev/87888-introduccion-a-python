# Tkinter (Es una librería para crear interfaces gráficas) GUI
# GUI -> Graphical User Interface (Interfaz gráfica)
# Es un librería buildin (Incorparada dentro del lenguaje)
# Set de componentes de interfaz gráficas (Ventanas, botones, campo de texto, etc)

class Persona:
    """ Un molde para crear personas """

    """ Constructor -> Es un método por defecto que se ejecuta al instanciar la clase"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """ Un método es una acción que la persona puede hacer (comportamiento) """
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


# Creamos 2 instancia a partir del molde

persona1 = Persona("Laura", 25) # persona1 es una instancia de Persona
persona2 = Persona("Eduymar", 20) # persona2 es otra instancia de Persona

print(persona1.presentarse())
print(persona2.presentarse())
