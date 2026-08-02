class Alternativa:
    def __init__(self, contenido, ayuda=""):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        print(f"Contenido: {self.contenido}")

        if self.ayuda != "":
            print(f"Ayuda: {self.ayuda}")