from pregunta import Pregunta


class Encuesta:
    def __init__(self, nombre, listado_preguntas=None):
        if listado_preguntas is None:
            listado_preguntas = []
        self.nombre = nombre
        self.listado_preguntas = []
        for pregunta in listado_preguntas:
            nueva_pregunta = Pregunta(
                pregunta["enunciado"],
                pregunta["ayuda"],
                pregunta["requerida"],
                pregunta["alternativas"]
            )
            self.listado_preguntas.append(nueva_pregunta)
        self.listados_respuestas = []

    def mostrar_encuesta(self):
        print(f"Encuesta: {self.nombre}")
        print("")
        for pregunta in self.listado_preguntas:
            pregunta.mostrar_pregunta()
            print()

    def agregar_listado_respuestas(self, listado):
        self.listados_respuestas.append(listado)


class EncuestaPorEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, listado_preguntas=None):
        super().__init__(nombre, listado_preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado):
        edad = listado.usuario.edad
        if edad >= self.edad_minima and edad <= self.edad_maxima:
            self.listados_respuestas.append(listado)
        else:
            print("El usuario no cumple con el rango de edad.")


class EncuestaPorRegion(Encuesta):
    def __init__(self, nombre, regiones, listado_preguntas=None):
        super().__init__(nombre, listado_preguntas)
        self.regiones = regiones

    def agregar_listado_respuestas(self, listado):
        if listado.usuario.region in self.regiones:
            self.listados_respuestas.append(listado)
        else:
            print("La región del usuario no está permitida.")