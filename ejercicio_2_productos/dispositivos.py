from .excepciones import StockInvalidoError

class DispositivoEcologico:
    def __init__(self, id_producto, nombre, precio, stock) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock= 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                f"El producto {self.nombre} no puede ser un valor negativo."
                f"Valor intentado: {valor}"
                )
        self._stock = valor

    def generar_ficha_tecnica(self):
        return {
            "id_producto":self.id_producto,
            "nombre": self.nombre,
            "precio" : f"${self.precio:.2f}",
            "stock": self.stock
        }

class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha= super().generar_ficha_tecnica()
        ficha.update({
            "eficiencia": self.eficiencia,
            "potencia_w": self.potencia_w
        })
        return ficha
    