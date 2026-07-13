from masa import escoger_masa
from salsa import escoger_salsa
from ingredientes import escoger_ingredientes

# Listas
masas = ["1 = Masa Tradicional", "2 = Masa Delgada", "3 = Masa con Bordes de Queso"]
salsas = ["1 = Salsa de Tomate", "2 = Salsa Alfredo", "3 = Salsa Barbecue", "4 = Salsa Pesto"]
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
#  Guardado de eleccion usuario
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
    elif opcion_del_panel_principal == "2":
        salsa_escogida = escoger_salsa(salsas)
    elif opcion_del_panel_principal == "3":
        ingredientes_pizza = escoger_ingredientes(ingredientes, ingredientes_pizza)
    elif opcion_del_panel_principal == "4":
        print("Elimine ingredientes")
        if not ingredientes_pizza:
            print("Sin ingredientes seleccionados")
        else:
            for posicion_de_nombres_internos in ingredientes_pizza:
                print(ingredientes[posicion_de_nombres_internos - 1])
            ingrediente_a_eliminar = int(input("Seleccione el ingrediente que desea eliminar: "))
            if ingrediente_a_eliminar in ingredientes_pizza:
                ingredientes_pizza.remove(ingrediente_a_eliminar)
                print("Ingrediente eliminado")
            else:
                print("Ingrediente no esta en su pizza")
    elif opcion_del_panel_principal == "5":  # Actualmente en Obras
        texto_masa_escogida = "Sin masa seleccionada"
        texto_salsa_escogida = "Sin salsa seleccionada"
        nombres_internos_ingredientes_pizza = []
        if masa_escogida != 0:
            texto_masa_escogida = masas[masa_escogida - 1]
        if salsa_escogida != 0:
            texto_salsa_escogida = salsas[salsa_escogida - 1]
        for posicion_de_nombres_internos in ingredientes_pizza:
            nombres_internos_ingredientes_pizza.append(nombres_ingredientes[posicion_de_nombres_internos - 1])
        print(f"Su pizza actualmente luce asi: {texto_masa_escogida}, {texto_salsa_escogida}, {nombres_internos_ingredientes_pizza}\nPara cambiar la masa o la salsa, solo ingrese de nuevo a su categoria correspondiente y elija de nuevo (lo mismo para agregar ingredientes nuevos).\nPara eliminar ingredientes escoja la opción 4.\nPara CONFIRMAR SU PEDIDO, presione 6.")
    elif opcion_del_panel_principal == "6":
        print("Pedido Confirmado. Gracias por preferirnos")
        exit()
    elif opcion_del_panel_principal == "7":
        exit()
    else:
        print("Escoja solo una opción mostrada en pantalla")
"""
# dale un tiempo estimado de preparacion
"""
