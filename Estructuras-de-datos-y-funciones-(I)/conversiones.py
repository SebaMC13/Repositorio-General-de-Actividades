import sys

#tasas de convercion en distintas monedas y valor ingresado por usuario en pesos chilenos
tasa_conversion_soles_peruanos = float(sys.argv[1])
tasa_conversion_pesos_argentinos = float(sys.argv[2])
tasa_conversion_dolares_americanos = float(sys.argv[3])
pesos_chilenos = int(sys.argv[4])

#calculadora de valores
soles_peruanos = tasa_conversion_soles_peruanos * pesos_chilenos
pesos_argentinos = tasa_conversion_pesos_argentinos * pesos_chilenos
dolares_americanos = tasa_conversion_dolares_americanos * pesos_chilenos

#Resultados mostrados al usuario
print(f"Los {pesos_chilenos} pesos equivalen a:\n{soles_peruanos} Soles\n{pesos_argentinos} Pesos Argentinos\n{dolares_americanos} Dólares")
