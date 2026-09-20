# estructuras/excepciones.py

class EstructuraVaciaError(Exception):
    """Se lanza al intentar eliminar de una estructura vacía."""
    pass

class Estalleno(Exception):
    """Se lanza al intentar insertar en una estructura llena (estática)."""
    pass