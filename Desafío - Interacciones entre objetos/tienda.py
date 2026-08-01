from abc import ABC, abstractmethod


class Tienda(ABC):
    def __init__(self, nombre, producto):
        self._nombre = nombre
        self._delivery = 0
        self._lista = []
        self._lista.append(producto)

    @abstractmethod
    def ingresar_producto(self):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass


class Restaurante(Tienda):
    def __init__(self):
        super().__init__()

    def listar_productos(self):
        return ...

    def realizar_venta(self, nombre_producto, cantidad):
        return ...


class Supermercado(Tienda):
    def __init__(self):
        super().__init__()

    def listar_productos(self):
        return ...

    def realizar_venta(self, nombre_producto, cantidad):
        return ...


class Farmacia(Tienda):
    def __init__(self):
        super().__init__()

    def listar_productos(self):
        return ...

    def realizar_venta(self, nombre_producto, cantidad):
        return ...


medicamento = Producto(
    "medicamento", 10_00, -5
)  # posible ejemplo? no se si es necesario en el desafio
print(medicamento.stock)
medicamento.stock = -10
print(medicamento.stock)
