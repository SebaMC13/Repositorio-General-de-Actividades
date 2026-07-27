from te import Te

te_1 = Te(1, 300)
te_2 = Te(3, 500)

tipo_1 = type(te_1)
tipo_2 = type(te_2)

print(tipo_1)
print(tipo_2)

if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")