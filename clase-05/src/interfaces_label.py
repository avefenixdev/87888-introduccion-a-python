import tkinter as tk

# Creamos la ventana
ventana = tk.Tk()

# Configuramos
ventana.title("Mi App con label")
ventana.geometry("800x600")

# Creamos la etiqueta
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack() # Mostrar en la interfaz la etiqueta

ventana.mainloop()

