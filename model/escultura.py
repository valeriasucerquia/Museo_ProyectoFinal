from model.obraDeArte import ObraDeArte

class Escultura(ObraDeArte):
    def __init__(self, nombre, autor, en_venta, volumen, material):
        super().__init__(nombre, autor, en_venta)
        self.__volumen = volumen
        self.__material = material

    @property #Get
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, volumen):
        self.__volumen = volumen

    @property #Get
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material
