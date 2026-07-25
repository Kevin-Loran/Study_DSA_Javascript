import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fimDaFila = -1
        self.fila = np.empty(capacidade, dtype=int)

    def enfileirar(self, valor):
        if self.fimDaFila  == self.capacidade - 1:
            return "fila cheia."
        else:
            self.fimDaFila += 1
            self.fila[self.fimDaFila] = valor

    def desenfileirar(self):
        if self.fimDaFila == - 1:
            return "fila vazia."
        else:
            for i in range(self.fimDaFila):
                self.fila[i] = self.fila[i + 1]
            self.fimDaFila -= 1


    def ver_inicio(self):
        if self.fimDaFila == -1:
            return -1
        return self.fila[0]


fila = Fila(5)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
print(fila.enfileirar(7))
print(fila.ver_inicio())
print(len(fila.fila))
