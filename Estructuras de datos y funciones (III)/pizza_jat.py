from masa import escoger_masa
from salsa import escoger_salsa
from ingredientes import escoger_ingredientes

# Listas
masas = ["1 = Masa Tradicional", "2 = Masa Delgada", "3 = Masa con Bordes de Queso"]
salsas = [
    "1 = Salsa de Tomate",
    "2 = Salsa Alfredo",
    "3 = Salsa Barbecue",
    "4 = Salsa Pesto",
]
ingredientes = [
    "1 = Tomate",
    "2 = Champiñones",
    "3 = Aceituna",
    "4 = Cebolla",
    "5 = Pollo",
    "6 = Jamón",
    "7 = Carne",
    "8 = Tocino",
    "9 = Queso",
]
nombres_ingredientes = [
    "Tomate",
    "Champiñones",
    "Aceituna",
    "Cebolla",
    "Pollo",
    "Jamón",
    "Carne",
    "Tocino",
    "Queso",
]
# Guardado de eleccion usuario
masa_escogida = 0
salsa_escogida = 0
ingredientes_pizza = []

# Inicio del programa

opcion_del_panel_principal = " "
while opcion_del_panel_principal != "7":
    print("- - - PIZZA JAT - - -\nEsta dentro del menu interactivo de Pizza JAT")
    print("1 = Cambiar masa")
    print("2 = Cambiar salsa")
    print("3 = Agregar ingrediente")
    print("4 = Eliminar ingrediente")
    print("5 = Ver pizza")
    print("6 = Confirmar pedido")
    print("7 = Salir")
    print("")
    opcion_del_panel_principal = input("Seleccione un numero de Opción en pantalla: ")
    print("")
    if opcion_del_panel_principal == "1":
        masa_escogida = escoger_masa(masas)
        print("")
    elif opcion_del_panel_principal == "2":
        salsa_escogida = escoger_salsa(salsas)
        print("")
    elif opcion_del_panel_principal == "3":
        ingredientes_pizza = escoger_ingredientes(ingredientes, ingredientes_pizza)
        print("")
    elif opcion_del_panel_principal == "4":
        print("Eliminar ingredientes")
        if not ingredientes_pizza:
            print("Sin ingredientes seleccionados")
        else:
            while True:
                for posicion_de_nombres_internos in ingredientes_pizza:
                    print(ingredientes[posicion_de_nombres_internos - 1])
                try:
                    ingrediente_a_eliminar = int(
                        input("Seleccione el ingrediente que desea eliminar: ")
                    )
                except ValueError:
                    print("Debe ingresar un número de ingrediente")
                    continue
                if ingrediente_a_eliminar in ingredientes_pizza:
                    ingredientes_pizza.remove(ingrediente_a_eliminar)
                    print("Ingrediente eliminado")
                    break
                else:
                    print("El Ingrediente no está en su pizza")
        print("")
    elif opcion_del_panel_principal == "5":
        texto_masa_escogida = "Sin masa seleccionada"
        texto_salsa_escogida = "Sin salsa seleccionada"
        nombres_internos_ingredientes_pizza = []
        if masa_escogida != 0:
            texto_masa_escogida = masas[masa_escogida - 1]
        if salsa_escogida != 0:
            texto_salsa_escogida = salsas[salsa_escogida - 1]
        for posicion_de_nombres_internos in ingredientes_pizza:
            nombres_internos_ingredientes_pizza.append(
                nombres_ingredientes[posicion_de_nombres_internos - 1]
            )
        print(
            f"Su pizza actualmente luce asi: {texto_masa_escogida}, {texto_salsa_escogida}, {nombres_internos_ingredientes_pizza}\nPara cambiar la masa o la salsa, solo ingrese de nuevo a su categoria correspondiente y elija de nuevo (lo mismo para agregar ingredientes nuevos).\nPara eliminar ingredientes escoja la opción 4.\nPara CONFIRMAR SU PEDIDO, presione 6."
        )
    elif opcion_del_panel_principal == "6":
        tiempo_preparacion = 20 + len(ingredientes_pizza) * 2
        print(f"Su pizza actualmente tardará {tiempo_preparacion} min.")
        while True:
            eleccion_final = input("Desea Confirmar su Pedido: Si / No ").lower()
            if eleccion_final == "si":
                print("Pedido Confirmado. Gracias por preferirnos")
                exit()
            elif eleccion_final == "no":
                print(
                    "Pedido Cancelado. ¡Gracias por visitarnos, que tengas un excelente día!"
                )
                exit()
            else:
                print("Elija solo una de las 2 opciones presentadas (Si o No) ")
    elif opcion_del_panel_principal == "7":
        print("¡Gracias por visitarnos, que tengas un excelente día!")
        exit()
    else:
        print("Escoja solo una opción mostrada en pantalla")
