import numpy as np

class Fila_prioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fimDaFila = -1
        self.fila = np.empty(capacidade, dtype=int)

    def filaVazia(self):
        if self.fimDaFila == -1:
            return True
        return False

    def filaCheia(self):
        if self.fimDaFila == self.capacidade - 1:
            return True
        return False

    def posicao(self, valor):
        for i in range(self.fimDaFila + 1):
            if valor < self.fila[i]:
                return i
        return self.fimDaFila + 1

    def enfileirar(self, valor):
        if self.filaCheia():
            return "Fila cheia"

        posicao = self.posicao(valor)
        i = self.fimDaFila

        while i >= posicao:
            self.fila[i + 1] = self.fila[i]
            i -= 1

        self.fila[posicao] = valor
        self.fimDaFila += 1

    def pesquisar(self, valor):
        if self.filaVazia():
            return "Fila Vazia"

        for i in range(self.fimDaFila + 1):
            if self.fila[i] == valor:
                return i
        return -1
    
    def desenfileirar(self):
        if self.filaVazia():
            print("lista vazia")
            return -1
        self.fimDaFila -= 1


fila = Fila_prioridade(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(10)
fila.enfileirar(8)
fila.desenfileirar()

for i in range(fila.fimDaFila + 1):
    print(fila.fila[i])