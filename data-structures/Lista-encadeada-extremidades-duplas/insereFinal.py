class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.ultimo = novo
        self.ultimo = novo

    def mostrar(self):
        if self.__lista_vazia():
            print("lista vazia.")
            return
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo

lista = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.mostrar()
