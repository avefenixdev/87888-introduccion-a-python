import tkinter as tk

# Creo ventana
ventana = tk.Tk()

# Configuro la ventana
ventana.title("Mi App")
ventana.geometry("800x600")

# Función que queremos que se ejecute cuando se presione el botón
def al_presionar():
    print("¡Presionaste el botón!")

# Construimos el botón
boton = tk.Button(ventana, text="Presione aquí", command=al_presionar)
boton.pack()

# Iniciamos la app
ventana.mainloop()
