def media(array):
    somador = 0
    for i in range(len(array)):
        somador += array[i]

    media = somador / len(array)
    return media

array = [10, 8, 7, 5]
print(media(array))
