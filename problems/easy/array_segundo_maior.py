def segundoMaior(array):
    maior = 0
    segundoMaior = 0
    arrayOrdenado = sorted(array)
    for numeros in arrayOrdenado:
        if numeros > maior:
            segundoMaior = maior
            maior = numeros

    return segundoMaior

array = [10, 5, 8, 10, 3]
print(segundoMaior(array))