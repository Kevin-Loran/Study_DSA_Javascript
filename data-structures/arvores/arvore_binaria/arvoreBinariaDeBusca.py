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
            self.raiz = novo
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
            if node is None:
                return

        if node.left:
            print("(", end="")
            self.simetric_traversal(node.left)
        print(node.valor, end="")
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")

    def pesquisa(self, valor):
        atual = self.raiz
        while atual is not None:
            if valor == atual.valor:
                return atual
            if valor < atual.valor:
                atual = atual.left
            else:
                atual = atual.right
        return None

    def pre_ordem(self, no):
        if no is not None:
            print(no.valor, end=" ")
            self.pre_ordem(no.left)
            self.pre_ordem(no.right)

    def ordem(self, no):
        if no is not None:
            self.ordem(no.left)
            print(no.valor, end=" ")
            self.ordem(no.right)

    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.left)
            self.pos_ordem(no.right)
            print(no.valor, end=" ")

    def exclusao(self, valor):
        if self.raiz is None:
            print("A árvore está vazia.")
            return False

        atual = self.raiz
        pai = self.raiz
        e_esquerda = True

        while atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.left
            else:
                e_esquerda = False
                atual = atual.right
            if atual is None:
                return False

        if atual.left is None and atual.right is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.left = None
            else:
                pai.right = None
        elif atual.right is None:
            if atual == self.raiz:
                self.raiz = atual.left
            elif e_esquerda:
                pai.left = atual.left
            else:
                pai.right = atual.left
        elif atual.left is None:
            if atual == self.raiz:
                self.raiz = atual.right
            elif e_esquerda:
                pai.left = atual.right
            else:
                pai.right = atual.right
        else:
            sucessor = self.getSucessor(atual)

            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.left = sucessor
            else:
                pai.right = sucessor

            sucessor.left = atual.left

        return True

    def getSucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.right
        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.left
        if sucessor != no.right:
            pai_sucessor.left = sucessor.right
            sucessor.right = no.right
        return sucessor


arvore = ArvoreBinaria()
arvore.inserir(11)
arvore.inserir(14)
arvore.inserir(9)
arvore.inserir(10)
arvore.inserir(24)

print("Simétrico com parênteses:")
arvore.simetric_traversal()
print("\n")

print("Em-Ordem (Crescente):")
arvore.ordem(arvore.raiz)
print("\n")

print("Pré-Ordem:")
arvore.pre_ordem(arvore.raiz)
print("\n")

print("Pós-Ordem:")
arvore.pos_ordem(arvore.raiz)