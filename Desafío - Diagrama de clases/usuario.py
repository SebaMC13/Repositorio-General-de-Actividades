from listado_respuestas import ListadoRespuestas


class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta, respuestas):
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado)