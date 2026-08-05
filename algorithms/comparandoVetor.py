import numpy as np
import timeit


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade atingida")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

def insere_ordenado(valores):
    vetor = VetorOrdenado(len(valores))
    for valor in valores:
        vetor.insere(valor)

vetorTeste = np.random.randint(1, 10001, 5000)
tempoVetor = timeit.timeit(
    lambda: insere_ordenado(vetorTeste.copy()), number=1
)

print(f"o valor de tempo de execução desse vetor é: {tempoVetor:.4f} S")