from model.obraDeArte import ObraDeArte

class Pintura(ObraDeArte):
    def __init__(self, nombre, autor, en_venta, dimensiones, tecnica, retrato):
        super().__init__(nombre, autor, en_venta)
        self.__dimensiones = dimensiones # Variable privada
        self.__tecnica = tecnica
        self.__retrato = retrato

    @property #Get
    def dimensiones(self):
        return self.__dimensiones

    @dimensiones.setter
    def dimensiones(self, dimensiones):
        self.__dimensiones = dimensiones

    @property #Get
    def tecnica(self):
        return self.__tecnica

    @tecnica.setter
    def tecnica(self, tecnica):
        self.__tecnica = tecnica

    @property #Get
    def retrato(self):
        return self.__retrato

    @retrato.setter
    def retrato(self, retrato):
        self.__retrato = retrato
