from .interfaces import Estructura
from typing import Any

class Nodo:
    def __init__(self, dato: Any):
        self.dato = dato
        self.siguiente = None

class ListaDinamica(Estructura):
    def __init__(self):
        self.cabeza = None
        self._tamanio = 0

    def insertar(self, dato: Any) -> None:
        # Por defecto podemos definir que 'insertar' general sea al final
        self.insertar_al_final(dato)

    def insertar_al_inicio(self, dato: Any) -> None:
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self._tamanio += 1

    def insertar_al_final(self, dato: Any) -> None:
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamanio += 1

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def __len__(self) -> int:
        return self._tamanio

    def __str__(self) -> str:
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return str(elementos)