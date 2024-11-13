from typing import Generic, TypeVar

T = TypeVar('T')

class GenericDTO(Generic[T]):
    def __init__(self, content: T = None):
        self._content = content

    def get_content(self) -> T:
        return self._content

    def set_content(self, content: T):
        self._content = content