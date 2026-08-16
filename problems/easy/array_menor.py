def numeroMenor(array):
    menor = 99999999999
    for numeros in array:
        if numeros < menor:
            menor = numeros
    return menor

array = [4, -10, 18, 10, 6]

menor = numeroMenor(array)
print("O menor número do array é ", menor)
