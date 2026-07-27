from te import Te

print("Escoja una de las 3 variedades de Té disponible:\n1 = Té negro\n2 = Té verde\n3 = Agua de hierbas")
te_escogido = int(input("Ingrese el numero escogido: "))
print("")
print("Escoja la cantidad de Gramos del Té seleccionado:\n500 gr\n300 gr")
gramos_escogidos = int(input("Ingrese la cantidad escogida: "))

minutos_te, recomendaciones = Te.tiempo_recomendacion(te_escogido)
precio_formato = Te.formato_gr(gramos_escogidos)

if te_escogido == 1:
    te_escogido = "Té negro"
elif te_escogido == 2:
    te_escogido = "Té verde"
elif te_escogido == 3:
    te_escogido = "Agua de hierbas"
print("")
print(f"Has elegido lo siguiente:\nSabor del tipo de té: {te_escogido}\nFormato: {gramos_escogidos} gr\nPrecio: {precio_formato}\nTiempo: {minutos_te} min\nRecomendación: {recomendaciones}")
