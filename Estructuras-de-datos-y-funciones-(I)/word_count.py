import sys
ruta_archivo = sys.argv[1]

with open(ruta_archivo, "r", encoding="utf-8") as file:
    lorem_ipsum = file.read()

#print(lorem_ipsum)

texto = lorem_ipsum
print(f"{len(texto)}")

