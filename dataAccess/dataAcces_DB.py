# dataAccess/datAcces_DB.py
import json
import os
from dtoGenerics.generic import GenericDTO

class DataAccessDB:
    def __init__(self, db_path='./database/obras.json'):
        self.db_path = db_path
        # Aseguramos que el archivo exista y esté inicializado
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_artwork(self, dto: GenericDTO):
        """Guarda una obra de arte representada por un DTO en el archivo JSON."""
        data = self.load_all_artworks()
        data.append(dto.get_content())
        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True

    def load_all_artworks(self):
        """Carga todas las obras de arte desde el archivo JSON."""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as file:
                # Verificamos si el archivo está vacío
                if os.path.getsize(self.db_path) == 0:
                    return []
                return json.load(file)
        except json.JSONDecodeError:
            # Si ocurre un error de decodificación, devolvemos una lista vacía
            return []
    
    def save_all_artworks(self, data):
        """Sobreescribe la información actualizada de la obra de arte en el archivo JSON."""
        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
