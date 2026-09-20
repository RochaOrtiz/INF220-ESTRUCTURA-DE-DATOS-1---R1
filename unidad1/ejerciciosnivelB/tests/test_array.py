import unittest
from estructura.array_estatico import ArrayEstatico
from estructura.excepcion import Estalleno


class TestArrayEstatico(unittest.TestCase):

    def test_creacion_y_vacio(self):
        """Prueba que el array se cree vacío y con la capacidad correcta."""
        arr = ArrayEstatico(3)
        self.assertTrue(arr.esta_vacia())
        self.assertEqual(len(arr), 0)
        self.assertEqual(arr.capacidad, 3)

    def test_insercion(self):
        """Prueba que los elementos se inserten y aumenten el tamaño."""
        arr = ArrayEstatico(2)
        arr.insertar("A")
        self.assertFalse(arr.esta_vacia())
        self.assertEqual(len(arr), 1)

        arr.insertar("B")
        self.assertEqual(len(arr), 2)

    def test_desbordamiento(self):
        """Prueba que se lance la excepción Estalleno al superar la capacidad."""
        arr = ArrayEstatico(1)
        arr.insertar("Único")

        with self.assertRaises(Estalleno):
            arr.insertar("Demasiado")


if __name__ == "__main__":
    unittest.main()