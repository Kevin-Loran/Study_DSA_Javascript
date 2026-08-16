def unicoCaractere(string):
    for letras in string:
        contador = 0
        comparador = letras
        for letras in string:
            if letras == comparador:
                contador += 1
        if contador == 1:
            return comparador


print(unicoCaractere("swiss"))