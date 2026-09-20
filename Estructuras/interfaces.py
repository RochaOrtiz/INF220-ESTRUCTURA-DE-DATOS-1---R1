from abc import ABC, abstractmethod
from typing import Any

class EstructuraEstatica(ABC):
    """Interfaz base para las estructuras lineales."""

    @abstractmethod
    def insertar (self , dato: Any):
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def esta_vacia (self):
        """Retorna True si la estructura está vacía."""
        pass
    
    @abstractmethod
    def __len__ (self):
        """Retorna la cantidad de elementos."""
        pass