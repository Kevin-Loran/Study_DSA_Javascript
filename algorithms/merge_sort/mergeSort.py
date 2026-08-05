import numpy as np

def merge_sort(vetor):
    if len(vetor) > 1:
        divisor = len(vetor) // 2
        esquerda = vetor[:divisor].copy()
        direita = vetor[divisor:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
        return vetor

print(merge_sort(np.array([15, 67, 30, 25])))