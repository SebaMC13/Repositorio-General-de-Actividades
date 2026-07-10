# Listas
masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
ingredientes = [
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
# Listas de guardado
masa_escogida = " "
salsa_escogida = " "
ingrediente_escogido = " "

# Inicio del programa
print("- - PIZZA JAT - -\nEsta dentro del menu interactivo de Pizza JAT")
opcion_del_panel_principal = " "
while opcion_del_panel_principal != "7":
    print("1 = Cambiar masa")
    print("2 = Cambiar salsa")
    print("3 = Agregar ingrediente")
    print("4 = Eliminar ingrediente")
    print("5 = Ver pizza")
    print("6 = Confirmar pedido")
    print("7 = Salir")
    opcion_del_panel_principal = input("Seleccione un numero: ")
    if opcion_del_panel_principal == "1":
        print("Escoja una masa")
        for masa in masas:
        print(masa)
    masa_escogida = input("Seleccione una masa: ")
    elif opcion_del_panel_principal == "2":
        print("Escoja una salsa")
    elif opcion_del_panel_principal == "3":
        print("Escoja los ingredientes")
    elif opcion_del_panel_principal == "4":
        print("Elimine ingredientes")
    elif opcion_del_panel_principal == "5":
        print("Asi luce la pizza que acaba de preparar")
    elif opcion_del_panel_principal == "6":
        print("")
    else:
        print("Escoja una opción mostrada en pantalla")
# elige el tipo de masa
for masa in masas:
    print(masa)
masa_escogida = input("Escoge una Masa\n")
# elige el tipo de salsa
for salsa in salsas:
    print(salsa)
salsa_escogida = input("Escoge una Salsa\n")
# elige el tipo de ingredientes
for ingrediente in ingredientes:
    print(ingrediente)
ingrediente_escogido = input("Escoge tus Ingredientes\n")

# mostrar con esta su pizza actualmente
print(
    f"Su pizza actualmente luce asi: {masa_escogida}, {salsa_escogida}, {ingrediente_escogido}"
)
# dale un tiempo estimado de preparacion
# pedirle la confirmacion del pedido
