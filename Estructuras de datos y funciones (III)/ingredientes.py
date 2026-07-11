def escoger_ingredientes(ingredientes):
    ingredientes_pizza = []
    ingrediente_actual = 0
    while True:
        for ingrediente in ingredientes:
            print(ingrediente)
        try:
            ingrediente_actual = int(input("Seleccione los ingrediente de su pizza (0 para terminar): "))
        except ValueError:
            print("Debe ingresar un número")
            continue
        if ingrediente_actual == 0:
            return ingredientes_pizza
        if ingrediente_actual < 1 or ingrediente_actual > 9:
            print("Escoja solo las opciones mostrada en pantalla")
        else:
            ingredientes_pizza.append(ingrediente_actual)
            posicion_ingredientes = ingredientes[ingrediente_actual - 1]
            print(posicion_ingredientes)  # borrar despues
    return ingredientes_pizza