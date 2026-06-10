import tkinter as tk

ventana = tk.Tk()

ventana.title("Trabajando con parrafos")
ventana.geometry("400x300")

# Área de texto
texto = tk.Text(ventana, height=5, width=30) # Text Area
texto.pack()

def obtener_todo():
    contenido = texto.get("1.0", tk.END) # desde el inicio hasta al fin
    print(contenido)

boton = tk.Button(ventana, text="Ver texto", command=obtener_todo)
boton.pack()

ventana.mainloop()

## Gestión de layout

# 1. pack(): Apilar widgets (arriba-abajo - izq-der)
# 2. grid(): Coloca en filas y columnas
# 3. place(): Posición exacta (menos común)

