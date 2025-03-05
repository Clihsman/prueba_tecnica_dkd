import csv
import json

def convertir_csv_a_json(archivo_csv, archivo_json):
    # se abre  el archivo CSV para  la lectura
    with open(archivo_csv, mode='r', encoding='utf-8') as csv_file:
        # Lee el contenido del archivo CSV
        lector_csv = csv.DictReader(csv_file)
        
        # Convertimos el contenido en la lista
        lista_usuarios = [fila for fila in lector_csv]
        
    # Guardamos la lista de  como archivo JSON
    with open(archivo_json, mode='w', encoding='utf-8') as json_file:
        json.dump(lista_usuarios, json_file, indent=4, ensure_ascii=False)

# Llamada a la función de conversión (esto será usado al ejecutar el script)
if __name__ == "__main__":
    convertir_csv_a_json("usuarios.csv", "usuarios.json")