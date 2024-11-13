class ObraDeArte:
    def __init__(self, nombre, autor, en_venta):
        self._nombre = nombre # Variable protegida
        self._autor = autor # Variable protegida
        self._en_venta = en_venta # Variable protegida

    @property 
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property #Get
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property #Get
    def en_venta(self):
        return self._en_venta

    @en_venta.setter
    def en_venta(self, en_venta):
        self._en_venta = en_venta