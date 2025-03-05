
import unittest
from prueba_palindromo import obtener_palindromos

class TestPalindromos(unittest.TestCase):
    def test_palindromos(self):
        palabras = ["oso", "casa", "radar", "sol", "reconocer", "luz", "anilina"]
        self.assertEqual(obtener_palindromos(palabras), ["oso", "radar", "reconocer", "anilina"])

if __name__ == '__main__':
    unittest.main()
