def numeroMaior(array):
    maior = 0
    for numeros in array:
        if numeros > maior:
            maior = numeros
    return maior

array = [4, 7, 18, 10, 6]

maior = numeroMaior(array)
print("o maior número do array é: ", maior)