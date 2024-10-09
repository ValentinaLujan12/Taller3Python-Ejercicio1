from almacenamientos.** import **


class AlmacenamientoExterno:
    _cantidad = **

    def __init__ (self, nombre):
        self._nombre = nombre
        self._almacenamiento = Almacenamiento(1000, "HDD")
        **._cantidad += 1

    def **(**, **):
        self.** = **

    def **(**):
        return self.**

    def setAlmacenamiento(self, almacenamiento):
        self._almacenamiento = almacenamiento

    def getAlmacenamiento(self):
        return self._almacenamiento

    **
    def getCantidad(**):
        return cls._cantidad