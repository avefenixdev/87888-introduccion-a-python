import tkinter as tk

class MiApp:

    """ Constructor """
    def __init__(self, ventana):
        self.ventana = ventana
        # Configuro la ventana...
        self.ventana.title("Mi primera aplicación") # le coloco un título
        self.ventana.geometry("800x600") # unas dimensiones

    def iniciar(self):
        """ Mostrar la ventana """
        self.ventana.mainloop()


# Crear una ventana principal
ventana = tk.Tk()

# Creamos la aplicación
app = MiApp(ventana) # Instanciamos la clase MiApp -> Creamos el objeto

# Mostrar
app.iniciar()
