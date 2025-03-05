


def es_palindromo(palabra: str) -> bool:
    return palabra == palabra[::-1]

def obtener_palindromos(palabras: list[str]) -> list[str]:
    return list(filter(es_palindromo, palabras))

if __name__ == "__main__":
    palabras = ["oso", "casa", "radar", "sol", "reconocer", "luz", "anilina"]
    print("Palíndromos encontrados:", obtener_palindromos(palabras))