def intersecao(array1, array2):
    intersecao = []

    for i in range(len(array1)):
        comparativo = array1[i]
        for j in range(len(array2)):
            if comparativo == array2[j]:
                intersecao.append(comparativo)

    return intersecao

array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]

print(intersecao(array1, array2))