def escoger_masa(masas):
    masa_escogida = 0
    while masa_escogida < 1 or masa_escogida > 3:
        for masa in masas:
            print(masa)
        try:
            masa_escogida = int(input("Seleccione una masa: "))
        except ValueError:
            print("Debe ingresar un número")
            continue
        if masa_escogida < 1 or masa_escogida > 3:
            print("Escoja una de las opciones mostrada en pantalla")
        else:
            posicion_masas = masas[masa_escogida - 1]
            print(posicion_masas)  # borrar despues
    return masa_escogida
            