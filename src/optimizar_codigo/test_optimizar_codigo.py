import unittest
from optimizar_codigo import procesar_lista

class TestProcesarLista(unittest.TestCase):
    def test_lista_numeros(self):
        self.assertEqual(procesar_lista([5, 3, 8, 3, 1, 5, 2, 8, 1]), [1, 2, 3, 5, 8])
        self.assertEqual(procesar_lista([]), [])
        self.assertEqual(procesar_lista([1, 1, 1, 1]), [1])
        self.assertEqual(procesar_lista([10, 2, -1, 3, 2]), [-1, 2, 3, 10])

if __name__ == "__main__":
    unittest.main()