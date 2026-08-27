from abc import ABC, abstractmethod


class ListaADT(ABC):
    """Define las operaciones básicas de una lista."""

    @abstractmethod
    def agregar(self, dato: int) -> None:
        """Agrega un dato a la lista."""
        pass

    @abstractmethod
    def obtener(self, indice: int) -> int:
        """Obtiene un dato mediante su posición."""
        pass

    @abstractmethod
    def tamano(self) -> int:
        """Devuelve la cantidad de elementos."""
        pass


class MiLista(ListaADT):
    """Implementación sencilla del ADT Lista."""

    def __init__(self) -> None:
        self.datos: list[int] = []

    def agregar(self, dato: int) -> None:
        """Agrega un dato al final de la lista."""
        self.datos.append(dato)

    def obtener(self, indice: int) -> int:
        """Obtiene el dato ubicado en el índice indicado."""
        return self.datos[indice]

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""
        return len(self.datos)


def main() -> None:
    """Prueba las operaciones de la lista."""
    lista = MiLista()

    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    print("Tamaño de la lista:", lista.tamano())
    print("Elemento en posición 1:", lista.obtener(1))


if __name__ == "__main__":
    main()
