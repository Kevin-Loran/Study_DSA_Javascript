def removerDuplicado(array):
    j = 0
    while j < len(array):
        j += 1
        if j == len(array):
            break
        print("contador j:", j)
        comparativo = array[j]
        contagem = 0
        for i in range(len(array)):
            print("contador i: ", i)
            if comparativo == array[i]:
                contagem += 1
            if contagem > 1:
                array.pop(i)
                break

    return array

array = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(removerDuplicado(array))
