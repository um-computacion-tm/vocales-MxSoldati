def contar_vocales(palabra):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in palabra:
        if letra in vocales:
            if letra not in resultado.keys():  
                resultado[letra] = 1
            else: resultado[letra] += 1
    return resultado