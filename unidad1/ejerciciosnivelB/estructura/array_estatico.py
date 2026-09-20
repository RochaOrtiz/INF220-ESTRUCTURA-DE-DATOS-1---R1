from .interfaces import Estructura
from .excepcion import Estalleno
from typing import Any

class ArrayEstatico(Estructura):
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.tamanio_actual = 0

    def insertar(self, dato: Any) -> None:
        if self.tamanio_actual >= self.capacidad:
            raise Estalleno("Error: El Array Estático está lleno.")
        self.elementos[self.tamanio_actual] = dato
        self.tamanio_actual += 1

    def esta_vacia(self) -> bool:
        return self.tamanio_actual == 0

    def __len__(self) -> int:
        return self.tamanio_actual

    def __str__(self) -> str:
        return str([self.elementos[i] for i in range(self.tamanio_actual)])