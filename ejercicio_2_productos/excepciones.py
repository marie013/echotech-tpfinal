class StockInvalidoError(Exception):
    """El stock no puede ser un valor negativo"""
    def __init__(self, mensaje="El stock no puede ser un valor negativo" ):
        super().__init__(mensaje)