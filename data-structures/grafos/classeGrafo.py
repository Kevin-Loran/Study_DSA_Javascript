class Vertice:
     def __init__(self, rotulo):
         self.rotulo = rotulo
         self.visitado = False
         self.adjacentes = []

     def adiciona_adjacentes(self, adjacente):
         self.adjacentes.append(adjacente)

     def mostra_adjacentes(self):
         for i in self.adjacentes:
             print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo