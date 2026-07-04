responde_estimulo = (input("Responde a estímulos? (si/no) "))

while responde_estimulo != "si" and responde_estimulo != "no": #aseguranos de que la respuesta es adecuada
    responde_estimulo = (input("ingrese una respuesta adecuada. Responde a estímulos? (si/no) "))
if responde_estimulo == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir la via aerea")

    respira = (input("Respira? (si/no) "))

    while respira != "si" and respira != "no":
        respira = (input("Ingrese una respuesta adecuada. Respira? (si/no) "))
    if respira == "si":
        print("Permitirle posicion de suficiente ventilacion")
    else:
        print("Administrar 5 Ventilaciones y llamar a Ambulancia")
        
        ambulancia = "no"
        while ambulancia == "no":

            signos_de_vida = input("Signos de vida? (si/no): ")

            while signos_de_vida !="si" and signos_de_vida != "no":
                signos_de_vida = (input("Ingrese una respuesta adecuada. Signos de Vida? (si/no) "))
            if signos_de_vida == "si":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia")
        
            ambulancia = input("¿Llegó la ambulancia? (si/no) ")
            while ambulancia != "si" and ambulancia != "no":
                ambulancia = (input("Ingrese una respuesta adecuada. ¿Llegó la ambulancia? (si/no) "))

        print("Fin")
        
        
