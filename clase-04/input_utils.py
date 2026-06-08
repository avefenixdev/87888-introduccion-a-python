def pedir_gasto():
    # Controlamos
    # 1. Que sea un número
    # 2. Que no sea una palabra
    # 3. Que no sea negativo
    while True:
        try:
            gasto = float(input("Ingreso un gasto (0 para terminar):"))
            if gasto < 0:
                print('Error: El gasto no puede ser negativo.')
            return gasto
        except ValueError:
            print("Error: ingrese un número válido.")