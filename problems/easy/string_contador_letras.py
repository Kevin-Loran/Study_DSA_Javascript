def contadorLetras(string):
    objeto = {}
    palavra = string.lower()
    for letra in palavra:
        comparador = letra
        contador = 0
        for letra in palavra:
            if letra == comparador:
                contador += 1
        objeto[comparador] = contador
    return objeto

print(contadorLetras('banana'))
