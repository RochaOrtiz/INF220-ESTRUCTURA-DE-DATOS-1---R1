import unittest
from estructura.lista_dinamica import ListaDinamica


class TestListaDinamica(unittest.TestCase):

    def test_creacion_y_vacio(self):
        """Prueba que la lista comience vacía y con tamaño 0."""
        lista = ListaDinamica()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)

    def test_insercion_al_inicio(self):
        """Prueba insertar elementos al comienzo de la lista."""
        lista = ListaDinamica()
        lista.insertar_al_inicio(20)
        lista.insertar_al_inicio(10)

        self.assertEqual(len(lista), 2)
        self.assertFalse(lista.esta_vacia())
        self.assertEqual(str(lista), "[10, 20]")

    def test_insercion_al_final(self):
        """Prueba insertar elementos al final de la lista."""
        lista = ListaDinamica()
        lista.insertar_al_final("X")
        lista.insertar_al_final("Y")

        self.assertEqual(len(lista), 2)
        self.assertEqual(str(lista), "['X', 'Y']")

    def test_insercion_general(self):
        """Prueba el método 'insertar' heredado de la interfaz (por defecto al final)."""
        lista = ListaDinamica()
        lista.insertar(1)
        lista.insertar(2)
        self.assertEqual(len(lista), 2)
        self.assertEqual(str(lista), "[1, 2]")


if __name__ == "__main__":
    unittest.main()