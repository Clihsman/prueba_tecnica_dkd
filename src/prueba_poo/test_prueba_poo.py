import unittest
from prueba_poo import Administrativo, PrestacionServicios, TerminoDirectivo,SALARIO_MINIMO, AUXILIO_TRANSPORTE


class TestSistemaControlUsuarios(unittest.TestCase):

    def test_administrativo(self):
        admin1 = Administrativo("MATHIAS", "MATHI21", 19)
        admin2 = Administrativo("MARISOL", "MAR16", 22)
        
        self.assertEqual(admin1.calcular_salario(), SALARIO_MINIMO + AUXILIO_TRANSPORTE)
        self.assertEqual(admin2.calcular_salario(), SALARIO_MINIMO + AUXILIO_TRANSPORTE)
    
    def test_prestacion_servicios(self):
        servicio1 = PrestacionServicios("MAIKER", "KER27", 26, 140, 1200)
        servicio2 = PrestacionServicios("JOSUE", "JOS02", 33, 135, 1500)
        
        self.assertEqual(servicio1.calcular_salario(), 140 * 1200)
        self.assertEqual(servicio2.calcular_salario(), 135 * 1500)
    
    def test_termino_directivo(self):
        directivo1 = TerminoDirectivo("MAXIMILIANO", "MAX18", 35, "Gerente")
        directivo2 = TerminoDirectivo("MARIANY", "ANY24", 40, "ING")
        
        self.assertEqual(directivo1.calcular_salario(), SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO))
        self.assertEqual(directivo2.calcular_salario(), SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO))

if __name__ == '__main__':
    unittest.main()