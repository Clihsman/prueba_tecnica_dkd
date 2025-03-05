def procesar_lista(numeros):
    return sorted(set(numeros))

numeros = [5, 3, 8, 3, 1, 5, 2, 8, 1]
resultado = procesar_lista(numeros)
print(resultado)