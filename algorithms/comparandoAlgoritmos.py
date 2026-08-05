import random
import timeit
import numpy as np

from algorithms.bubble_sort.bubbleSort import bubble_sort
from algorithms.insertion_sort.insertionSort import insertion_sort
from algorithms.merge_sort.mergeSort import merge_sort
from algorithms.quick_sort.quickSort import quick_sort
from algorithms.selection_sort.selectionSort import selectionSort
from algorithms.shell_sort.shellSort import shell_sort

vetorTeste = np.random.randint(1, 10001, 5000)

# Passa uma cópia (.copy()) e roda 1 vez (number=1)
tempoBubbleSort = timeit.timeit(
    lambda: bubble_sort(vetorTeste.copy()), number=1
)
tempoSelectionSort = timeit.timeit(
    lambda: selectionSort(vetorTeste.copy()), number=1
)
tempoInsertionSort = timeit.timeit(
    lambda: insertion_sort(vetorTeste.copy()), number=1
)
tempoShellSort = timeit.timeit(
    lambda: shell_sort(vetorTeste.copy()), number=1
)
tempoMergeSort = timeit.timeit(
    lambda: merge_sort(vetorTeste.copy()), number=1
)

vetor_quick = vetorTeste.copy()
tempoQuickSort = timeit.timeit(
    lambda: quick_sort(vetor_quick, 0, len(vetor_quick) - 1), number=1
)

print(
    "Velocidade de cada algoritmo para 5.000 elementos (em segundos):"
    f"\n   Bubble Sort:    {tempoBubbleSort:.4f}s"
    f"\n   Selection Sort: {tempoSelectionSort:.4f}s"
    f"\n   Insertion Sort: {tempoInsertionSort:.4f}s"
    f"\n   Shell Sort:     {tempoShellSort:.4f}s"
    f"\n   Merge Sort:     {tempoMergeSort:.4f}s"
    f"\n   Quick Sort:     {tempoQuickSort:.4f}s"
)