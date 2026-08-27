class EstructuraVaciaError(Exception):
    """Excepción para indicar que una estructura está vacía."""


class Pila:
    """Representa una pila de datos."""

    def __init__(self) -> None:
        self.datos: list[int] = []

    def apilar(self, dato: int) -> None:
        """Agrega un dato a la pila."""
        self.datos.append(dato)

    def desapilar(self) -> int:
        """
        Elimina y devuelve el último dato de la pila.

        Raises:
            EstructuraVaciaError: Si la pila está vacía.
        """
        if not self.datos:
            raise EstructuraVaciaError(
                "No se puede desapilar porque la pila está vacía."
            )

        return self.datos.pop()


def main() -> None:
    """Ejecuta una prueba del manejo de excepciones."""
    pila = Pila()

    pila.apilar(10)
    pila.apilar(20)

    print("Elemento eliminado:", pila.desapilar())
    print("Elemento eliminado:", pila.desapilar())

    try:
        pila.desapilar()
    except EstructuraVaciaError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
