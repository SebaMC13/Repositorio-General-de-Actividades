class ListadoRespuestas:
    def __init__(self, usuario, lista_respuestas=None):
        if lista_respuestas is None:
            lista_respuestas = []
        self.usuario = usuario
        self.lista_respuestas = lista_respuestas