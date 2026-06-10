import tkinter as tk

# Creo la ventana
ventana = tk.Tk()

# Configuro la ventana
ventana.title("Mi primera App")
ventana.geometry("400x300")

# creo el input y lo incorporo en la interfaz
entrada = tk.Entry(ventana) # input
entrada.pack()

def obtener_texto():
    texto = entrada.get() # obtengo lo ingreado en el input
    print(f"Escribiste {texto}")

# Creo el botón y lo incorporo en la ventana
boton = tk.Button(ventana, text="Enviar", command=obtener_texto)
boton.pack()

# Arranco la app
ventana.mainloop()
