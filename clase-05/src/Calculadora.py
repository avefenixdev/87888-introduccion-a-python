import tkinter as tk
import math

class Calculadora:

    def __init__(self, ventana):
        # Configuración de la ventana
        self.ventana = ventana
        self.ventana.title("Calculadora elemental")

        # Configuración de la interfaz
        self.crear_widgets()

    def iniciar(self):
        """ Mostramos la ventana """
        self.ventana.mainloop()

    def crear_widgets(self):
        """ Creamos los elementos visuales """

        # Display de resultados (Pantalla)
        self.pantalla = tk.Entry(self.ventana, font=("Arial", 20), justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Botones números

        numeros = [
            ["7", "8", "9", "/", "√"],
            ["4", "5", "6", "*", "^"],
            ["1", "2", "3", "-", "("],
            ["0", ".", "=", "+", ")"]
        ]

        self.operacion = ""
        """ Creación de botones """
        for fila_idx, fila in enumerate(numeros, start=1):
            # print(fila)
            for col_idx, numero in enumerate(fila):
                # print(numero)
                boton = tk.Button(
                    self.ventana,
                    text=numero,
                    font=("Arial", 18),
                    command=lambda n=numero: self.al_presionar_boton(n)
                )

                boton.grid(row=fila_idx, column=col_idx, padx=2, pady=2)

        """ Botón borrar último caracter """
        boton_borrar = tk.Button(
            self.ventana,
            text="⌫",
            font=("Arial", 18),
            command=self.borrar_caracter
        )
        boton_borrar.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

        """ Boton limpiar todo """
        boton_borrar = tk.Button(
            self.ventana,
            text="C",
            font=("Arial", 18),
            command=self.limpiar
        )
        boton_borrar.grid(row=5, column=2, columnspan=3, padx=2, pady=2)

    def al_presionar_boton(self, valor):
        """ Manejar presión de botones """

        if valor == "=":
           try:
                """ cuando valor sea = """
                resultado = eval(self.operacion)
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, resultado)
                self.operacion = str(resultado)
           except Exception:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")
                self.operacion = ""
        elif valor == "^":
            self.operacion += "**"
            self.pantalla.delete(0,tk.END)
            self.pantalla.insert(0, self.operacion.replace("**", "^"))
        elif valor == "√":
            self.operacion += f"math.sqrt({self.operacion})"
            self.pantalla.delete(0,tk.END)
            self.pantalla.insert(0, self.operacion.replace("math.sqrt", "√"))

        else:
            """ Cuando la operación sea diferente de = """
            self.operacion += valor # "125+20"
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, self.operacion)

    def borrar_caracter(self):
        """ Borramos el último caracter """
        self.operacion = self.operacion[:-1]
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.operacion)

    def limpiar(self):
        """ Limpiar pantalla """
        self.pantalla.delete(0, tk.END)
        self.operacion = ""

# Crear y ejecutar
ventana = tk.Tk()
app = Calculadora(ventana)
app.iniciar()
