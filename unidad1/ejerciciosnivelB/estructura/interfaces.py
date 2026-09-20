from abc import ABC, abstractmethod
from typing import Any

class Estructura(ABC):
    """Interfaz base para las estructuras lineales."""

    @abstractmethod
    def insertar(self, dato: Any) -> None:
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        """Retorna True si la estructura está vacía."""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        pass