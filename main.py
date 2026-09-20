from Estructuras import ArrayEstatico
from utils.visualizaciones import imprimir_estado


def main():
    mi_array = ArrayEstatico(3)
    mi_array.insertar("Manzana")
    mi_array.insertar("Pera")

    imprimir_estado(mi_array)


if __name__ == "__main__":
    main()