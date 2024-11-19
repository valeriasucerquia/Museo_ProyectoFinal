from typing import Generic, TypeVar

T = TypeVar('T') # TypeVar es una forma de declarar un tipo genérico

class GenericDTO(Generic[T]): 
    def __init__(self, content: T = None): # Aquí la clase GenericDTO hereda de Generic[T], lo que indica que es una clase genérica.
        self._content = content # Pueda almacenar cualquier tipo de objeto

    # Método retorna el contenido almacenado, asegurando que el tipo devuelto coincida con T.
    def get_content(self) -> T:
        return self._content

    # Permite actualizar el contenido, también en el tipo T.
    def set_content(self, content: T):
        self._content = content
        
# Este enfoque es útil para encapsular cualquier tipo de dato mientras se mantiene 
# la flexibilidad y el tipo seguro en Python.