def escoger_salsa(salsas):
    salsa_escogida = 0
    while salsa_escogida < 1 or salsa_escogida > 4:
        for salsa in salsas:
            print(salsa)
        try:
            salsa_escogida = int(input("Seleccione una salsa: "))
        except ValueError:
            print("Debe ingresar un número")
            continue
        if salsa_escogida < 1 or salsa_escogida > 4:
            print("Escoja una de las opciones mostradas en la pantalla")
            print("")
    return salsa_escogida
