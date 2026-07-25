import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__pilha = np.empty(capacidade, dtype="U1")

    def pilha_cheia(self):
        return self.__topo == self.__capacidade - 1

    def pilha_vazia(self):
        return self.__topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("Pilha cheia")
        else:
            self.__topo += 1
            self.__pilha[self.__topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha vazia")
            return None
        else:
            valor = self.__pilha[self.__topo]
            self.__topo -= 1
            return valor

    def ver_topo(self):
        if self.pilha_vazia():
            return None
        else:
            return self.__pilha[self.__topo]


def validar_expressao(expressao):
    pilha = Pilha(len(expressao))

    pares = {"}": "{", "]": "[", ")": "("}

    for caractere in expressao:

        if caractere in "{[(":
            pilha.empilhar(caractere)

        elif caractere in "}])":
            if pilha.pilha_vazia():
                return False

            topo = pilha.desempilhar()
            if topo != pares[caractere]:
                return False

    return pilha.pilha_vazia()




exp1 = "c[d]"
exp2 = "a{b[c]d}e"
exp3 = "a{b(c]d}e"
exp4 = "a[b{c}d]e}"
exp5 = "a{b(c)"

print("exp1:", validar_expressao(exp1))
print("exp2:", validar_expressao(exp2))
print("exp3:", validar_expressao(exp3))
print("exp4:", validar_expressao(exp4))
print("exp5:", validar_expressao(exp5))