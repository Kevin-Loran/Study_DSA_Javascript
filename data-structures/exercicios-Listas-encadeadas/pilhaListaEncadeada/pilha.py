class No:
    def __init__(self, valor):
        self.valor = valor
        self.__anterior = None

    def mostrar_no(self):
        print(self.valor)

class PilhaListaEncadeada:
    def __init__(self):
        self.__topo = None

    def __pilhaVazia(self):
        return self.__topo == None

    def empilhar(self, valor):
        novo = No(valor)
        novo.__anterior = self.__topo
        self.__topo = novo

    def desempilhar(self):
        if self.__pilhaVazia():
            print("Pilha vazia.")
            return
        self.__topo = self.__topo.__anterior

    def ver_topo(self):
       print(self.__topo.valor)


pilhaEncadeada = PilhaListaEncadeada()
pilhaEncadeada.empilhar(1)
pilhaEncadeada.empilhar(2)
pilhaEncadeada.empilhar(3)
pilhaEncadeada.empilhar(4)
pilhaEncadeada.desempilhar()
pilhaEncadeada.ver_topo()