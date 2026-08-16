def contarOcorrencia(array, comparativo):
    contagem = 0
    for numeros in array:
        if comparativo == numeros:
            contagem += 1
    return contagem

array = [4, 4, 18, 4, 6]
print(contarOcorrencia(array, 4))