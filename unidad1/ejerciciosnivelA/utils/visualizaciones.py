def imprimir_estado(Estructura):
    """Función auxiliar para mostrar de forma limpia el estado de cualquier estructura."""
    print(f"-> Elementos: {Estructura}")
    print(f"-> Cantidad actual: {len(Estructura)}")
    print(f"-> ¿Está vacía?: {Estructura.esta_vacia()}")
    print("-" * 30)