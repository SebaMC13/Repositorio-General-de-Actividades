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
print("PIZZA JAT")
menu_principal = input(
    "Esta dentro del menu interactivo de Pizza JAT. Por favor arme su pizza: Masas - Salsas - Ingredientes\n"
)

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
