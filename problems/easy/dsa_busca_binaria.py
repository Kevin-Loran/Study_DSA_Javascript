def buscaBinaria(array, target):
    arrayOrdenado = sorted(array)
    meio = len(array) // 2
    while True:
        if arrayOrdenado[meio] == target:
            return meio
        elif arrayOrdenado[meio] > target:
            arrayOrdenado= arrayOrdenado[:meio]
        elif arrayOrdenado[meio] < target:
            arrayOrdenado= arrayOrdenado[meio:]
        meio = len(arrayOrdenado) // 2

array = [2, 1, 4, 3, 7, 8, 1]
print(buscaBinaria(array, 7))