def buscaLinear(array, target):
    posicao = 0
    for i in range(len(array)):
        if array[i] == target:
            return posicao
        posicao += 1
    return -1

lista = [10, 20, 30, 40]
print(buscaLinear(lista, 30))