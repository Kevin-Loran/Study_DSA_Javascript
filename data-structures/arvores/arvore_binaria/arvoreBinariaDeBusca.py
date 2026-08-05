class No:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

    def mostrar_no(self):
        print(self.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = No(valor)
            return
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:
                    atual = atual.left
                    if atual is None:
                        pai.left = novo
                        return
                elif valor > atual.valor:
                    atual = atual.right
                    if atual is None:
                        pai.right = novo
                        return
                else:
                    return

    
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.raiz
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node.valor, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")


arvore = ArvoreBinaria()
arvore.inserir(11)
arvore.inserir(14)
arvore.inserir(9)
arvore.inserir(10)
arvore.inserir(24)
arvore.simetric_traversal()





