#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Interfaz con ABC
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod


class EstructuraLineal(ABC):
    """Interfaz para una estructura de datos lineal."""

    @abstractmethod
    def insertar(self, dato: int) -> None:
        """Inserta un dato en la estructura."""
        pass

    @abstractmethod
    def eliminar(self) -> int:
        """Elimina y devuelve un dato de la estructura."""
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Indica si la estructura está vacía."""
        pass


class Lista(EstructuraLineal):
    """Implementación sencilla de una estructura lineal."""

    def __init__(self) -> None:
        self.datos: list[int] = []

    def insertar(self, dato: int) -> None:
        """Agrega un dato al final de la lista."""
        self.datos.append(dato)

    def eliminar(self) -> int:
        """Elimina y devuelve el último dato."""
        return self.datos.pop()

    def esta_vacia(self) -> bool:
        """Comprueba si la lista está vacía."""
        return len(self.datos) == 0


def main() -> None:
    """Ejecuta una prueba de la estructura."""
    lista = Lista()

    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)

    print("¿La lista está vacía?", lista.esta_vacia())
    print("Elemento eliminado:", lista.eliminar())
    print("Datos restantes:", lista.datos)


if __name__ == "__main__":
    main()
