def somaIgualAnumeros(array, target):
    comparador2 = 0
    somadores = []
    for i in range(len(array)):
        comparador1 = array[i]

        if comparador1 + comparador2 == target:
            somadores.append(comparador1)
            somadores.append(comparador2)

        comparador2 = comparador1

    return somadores

array = [2, 7, 11, 15]
print(somaIgualAnumeros(array, 9))