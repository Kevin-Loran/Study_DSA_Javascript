def ordena(array):
    tamanho = len(array)

    for i in range(len(array)):
        for j in range(0, tamanho - i -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

array = [8, 5, 4, 9, 7]
print(ordena(array))


