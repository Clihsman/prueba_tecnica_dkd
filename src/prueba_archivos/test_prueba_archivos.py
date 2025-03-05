import json
import unittest
import os
from prueba_archivos import convertir_csv_a_json

class TestConversionCSVJson(unittest.TestCase):

    def setUp(self):
        # Asumimos que ya existe el archivo usuarios.csv
        self.csv_file = "usuarios.csv"
        self.json_file = "usuarios.json"

    def test_conversion(self):
        # Ejecutamos la conversión
        convertir_csv_a_json(self.csv_file, self.json_file)

        # Verificamos que el archivo JSON se haya creado correctamente
        self.assertTrue(os.path.exists(self.json_file), "El archivo JSON no se ha creado.")

        # Leemos el archivo JSON generado
        with open(self.json_file, mode='r', encoding='utf-8') as json_file:
            datos_json = json.load(json_file)

        # Datos esperados en el formato JSON
        datos_esperados = [
            {"id": "1", "nombre": "Mario", "edad": "30", "email": "mario@example.com"},
            {"id": "2", "nombre": "Ana", "edad": "25", "email": "ana@example.com"},
            {"id": "3", "nombre": "Luis", "edad": "40", "email": "luis@example.com"}
        ]

        # Comprobamos que los datos en el archivo JSON coincidan con los esperados
        self.assertEqual(datos_json, datos_esperados, "Los datos del archivo JSON no son correctos.")

    def tearDown(self):
        # Limpiamos el archivo JSON generado
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

if __name__ == "__main__":
    unittest.main()