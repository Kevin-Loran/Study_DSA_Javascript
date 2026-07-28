class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        return (self.valor)


class Lista_encadeada:
    def __init__(self):
        self.primeiro = None


no1 = No(5)
print(no1.mostrar_no())
