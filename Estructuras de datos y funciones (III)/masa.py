def escoger_masa(masas):
    masa_escogida = 0
    while masa_escogida < 1 or masa_escogida > 3:
        for masa in masas:
            print(masa)
        masa_escogida = int(input("Seleccione una masa: "))
        if masa_escogida < 1 or masa_escogida > 3:
            print("Escoja una opción mostrada en pantalla")
        else:
            posicion_masas = masas[int(masa_escogida) - 1]
            print(posicion_masas)  # borrar despues
    return masa_escogida
