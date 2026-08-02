from alternativa import Alternativa

class Pregunta:

    def __init__(self, enunciado, ayuda="", requerida=False, alternativas=[]):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = []
        for alternativa in alternativas:
            nueva_alternativa = Alternativa(
                alternativa["contenido"],
                alternativa["ayuda"]
            )
            self.alternativas.append(nueva_alternativa)

    def mostrar_pregunta(self):
        print(f"Pregunta: {self.enunciado}")
        if self.ayuda != "":
            print(f"Ayuda: {self.ayuda}")
        print("Alternativas:")
        for alternativa in self.alternativas:
            alternativa.mostrar_alternativa()