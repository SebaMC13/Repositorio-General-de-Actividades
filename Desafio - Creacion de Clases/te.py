class Te:
    duracion_te = 365
    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato

    @staticmethod
    def tiempo_recomendacion(sabor):
        if sabor == 1:
            return (3, "Desayuno")
        elif sabor == 2:
            return (5, "Medio Dia")
        elif sabor == 3:
            return (6, "Atardecer")
        else:
            return ("Ingrese un valor numerico valido")

    @staticmethod
    def formato_gr(formato):
        if formato == 500:
            return (5000)
        elif formato == 300:
            return (3000)
        else:
            return ("Ingrese un valor numerico valido")