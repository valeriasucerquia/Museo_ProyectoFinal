# controller/controllerObradeArte.py
from dataAccess.dataAcces_DB import DataAccessDB
from dtoGenerics.generic import GenericDTO
from model.pintura import Pintura
from model.escultura import Escultura

class ArtController:
    def __init__(self):
        self.data_access = DataAccessDB()

    def add_pintura(self, nombre, autor, en_venta, dimensiones, tecnica, retrato):
        pintura = Pintura(nombre, autor, en_venta, dimensiones, tecnica, retrato)
        pintura_dict = pintura.__dict__.copy()
        pintura_dict["tipo_de_obra"] = "pintura"  # Añadimos el tipo de obra
        dto = GenericDTO(pintura_dict)
        self.data_access.add_artwork(dto)

    def add_escultura(self, nombre, autor, en_venta, volumen, material):
        escultura = Escultura(nombre, autor, en_venta, volumen, material)
        escultura_dict = escultura.__dict__.copy()
        escultura_dict["tipo_de_obra"] = "escultura"  # Añadimos el tipo de obra
        dto = GenericDTO(escultura_dict)
        self.data_access.add_artwork(dto)
