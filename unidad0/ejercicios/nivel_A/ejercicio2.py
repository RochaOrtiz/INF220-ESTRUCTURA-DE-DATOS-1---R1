#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CODIGO QUE NO TIENE DOCSTRINGS NI TYPE HINTS.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ListaNumeros:
    def __init__(self):
        self.numeros = []

    def agregar(self, numero):
        self.numeros.append(numero)

    def obtener_promedio(self):
        if len(self.numeros) == 0:
            return 0

        return sum(self.numeros) / len(self.numeros)


lista = ListaNumeros()

lista.agregar(80)
lista.agregar(90)
lista.agregar(70)

print(lista.obtener_promedio())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CODIGO CORREGIDO
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ListaNumeros:
    """Representa una lista sencilla de números."""

    def __init__(self) -> None:
        """Inicializa una lista vacía de números."""
        self.numeros: list[float] = []

    def agregar(self, numero: float) -> None:
        """
        Agrega un número a la lista.

        Args:
            numero: Número que se desea agregar.
        """
        self.numeros.append(numero)

    def obtener_promedio(self) -> float:
        """
        Calcula el promedio de los números almacenados.

        Returns:
            El promedio de los números.

        Raises:
            ValueError: Si la lista está vacía.
        """
        if len(self.numeros) == 0:
            raise ValueError("La lista está vacía.")

        return sum(self.numeros) / len(self.numeros)


lista = ListaNumeros()

lista.agregar(80)
lista.agregar(90)
lista.agregar(70)

print("Promedio:", lista.obtener_promedio())
