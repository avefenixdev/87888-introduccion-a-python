import tkinter as tk

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
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Botones números

        numeros = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        self.operacion = ""

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

    def al_presionar_boton(self, valor):
        """ Manejar presión de botones """

        if valor == "=":
            """ cuando valor sea = """
            resultado = eval(self.operacion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
            self.operacion = ""
        else:
            """ Cuando la operación sea diferente de = """
            self.operacion += valor # "125+20"
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, self.operacion)

    def limpiar(self):
        print('limpiar')

# Crear y ejecutar
ventana = tk.Tk()
app = Calculadora(ventana)
app.iniciar()
