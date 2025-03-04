def procesar_lista(numeros):
    lista_unicos = []
    for num in numeros:
        if num not in lista_unicos:
            lista_unicos.append(num)
    lista_unicos.sort()
    return lista_unicos

numeros = [5, 3, 8, 3, 1, 5, 2, 8, 1]
resultado = procesar_lista(numeros)
print(resultado)