class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)

class FilaListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def fila_vazia(self):
        return self.primeiro == None

    def ver_inicio(self):
        if self.fila_vazia():
            print("Fila vazia.")
            return
        print(self.primeiro.valor)

    def enfileirar(self, valor):
        novo = No(valor)
        if self.fila_vazia():
            self.primeiro = novo
            self.ultimo = novo
            return
        self.ultimo.proximo = novo
        self.ultimo = novo

    def desenfileirar(self):
        if self.fila_vazia():
            print("A fila está vazia.")
            return
        self.primeiro = self.primeiro.proximo
        if self.primeiro == None:
            self.ultimo = None

    def ver_fila(self):
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo




fila = FilaListaEncadeada()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.ver_fila()