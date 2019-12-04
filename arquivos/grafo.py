class No:
    def __init__(self, inicial, peso):
        self.data = inicial
        self.peso = peso
        self.next = None

    def get_data(self):
        return self.data

    def setd_data(self, new):
        self.data = new

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new

    def get_peso(self):
        return self.peso


class lista:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def vazio(self):
        return self.head == None

    def add(self, valor, peso):
        no = No(valor, peso)
        no.set_next(self.head)
        self.head = no

    def addLast(self, valor):
        atual = self.head
        while True:
            if atual.get_next() == None:
                valor.set_next(None)
                atual.set_next(valor)
                return atual
            else:
                atual = atual.get_next()
        return None
    def size(self):
        count = 0
        atual = self.head
        while atual != None:
            count += 1
            atual = atual.get_next()
        return count

    def exite(self, valor):
        atual = self.head
        while atual != None:
            if atual.get_data() == valor:
                return True
            else:
                atual = atual.get_next()
        return False

    def procura(self, valor):
        atual = self.head
        while atual != None:
            if atual.get_data() == valor:
                return atual.get_data()
            else:
                atual = atual.get_next()
        return None
    def printa(self):
        atual = self.head
        while atual != None:
            print(atual.get_data(),end=" ")
            atual = atual.get_next()
        return None
    def remove(self, valor):
        atual = self.head
        anterior = None
        while atual != None:
            if atual.get_data() == valor:
                anterior.set_next(atual.get_next())
                return atual
            else:
                anterior = atual
                atual = atual.get_next()
        return None
    def removeFirst(self):
        if self.head !=  None:
            prim = self.head
            self.head = self.head.get_next()
            return prim.get_data()
        return  False



class vertice:
    def __init__(self, no, adjacencia):
        self.no = no
        self.adjacencia = adjacencia

    def get_valor(self):
        return self.valor

    def get_no(self):
        return self.no

    def set_no(self, valor):
        self.no = valor

    def get_adjacencias(self):
        return self.adjacencia

    def set_adjacencia(self, lista):
        self.adjacencia = lista

    def add_adjacencia(self, valor, peso):
        self.adjacencia.add(valor, peso)


class Grafo:
    def __init__(self, listaV):
        self.vertices = listaV

    def add_aresta(self, no, lista):
        self.vertices.append(vertice(no, lista))

    def get_vertices(self):
        return self.vertices

    def get_aresta_indice(self, indece):
        return self.vertices[indece]

    def get_vertice(self, valor):
        for i in self.vertices:
            if i.get_no().get_data() == valor:
                return i
        return None

    def busca_profundidade(self, vertice):
        visitados = []

        def dfs_recursiva(atual, destino):
            visitados.append(atual.get_no().get_data())
            if atual.get_no().get_data() == destino.get_no().get_data(): return visitados
            no_proximo = atual.get_adjacencias().get_head()
            if no_proximo == None and len(visitados) < len(self.vertices):
                no_proximo = self.get_vertice(visitados[len(visitados) - 1]).get_no()
            while no_proximo.get_data() in visitados:
                no_proximo = no_proximo.get_next()
            vertice = self.get_vertice(no_proximo.get_data())
            while vertice != None and no_proximo.get_data() not in visitados:
                dfs_recursiva(self.get_vertice(vertice.get_no().get_data()), destino)
                vertice = vertice.get_no().get_next()
            return None

        destino = self.get_vertice(vertice)
        inicio = self.vertices[0]

        dfs_recursiva(inicio, destino)
        return visitados

    def busca_profundidade(self, ini, vertice):

        visitados = []
        nao_tem_adj = []

        def dfs_recursiva(atual, destino):
            visitados.append(atual.get_no().get_data())
            if atual.get_no().get_data() == destino.get_no().get_data(): return visitados
            no_proximo = atual.get_adjacencias().get_head()
            while no_proximo == None:
                nao_tem_adj.append(atual.get_no().get_data())
                if len(visitados) > 1:
                    t = self.get_vertice(visitados[len(visitados) - 2]).get_adjacencias()
                    t.set_head(t.get_head().get_next())
                    no_proximo = self.get_vertice(visitados[len(visitados) - 2]).get_adjacencias().get_head()
                    visitados.pop(len(visitados) - 1)
                else:
                    t = self.get_vertice(visitados[len(visitados) - 1]).get_adjacencias()
                    t.set_head(t.get_head().get_next())
                    no_proximo = self.get_vertice(visitados[len(visitados) - 1]).get_adjacencias().get_head()

            while no_proximo.get_data() in visitados:
                no_proximo = no_proximo.get_next()
            vertice = self.get_vertice(no_proximo.get_data())
            while vertice != None and no_proximo.get_data() not in visitados:
                dfs_recursiva(self.get_vertice(vertice.get_no().get_data()), destino)
                vertice = vertice.get_no().get_next()
            return None

        destino = self.get_vertice(vertice)
        inicio = self.get_vertice(ini)
        try:
            dfs_recursiva(inicio, destino)
        except:
            return "Não alcançável"
        return visitados

    def verifica_se_exite(self,s,v):
        for i in s:
            if v in i:
                return True
        return False


    def busca_largura(self, vertice):
        lista = []
        visitados = []
        inicio = self.vertices[0]
        lista.append(inicio.get_no().get_data())
        t = inicio.get_adjacencias().get_head()
        visitados.insert(0, inicio.get_no().get_data())
        visitados.insert(0, t.get_data())
        k = inicio.get_adjacencias().get_head()
        while t != None:

            while k != None:
                if k.get_data() not in visitados:
                    lista.append(k.get_data())
                    visitados.insert(0,k.get_data())
                    if vertice in visitados:
                        return visitados
                k = k.get_next()
            lista.pop(0)
            t = t.get_next()
            k = self.get_vertice(t.get_data()).get_adjacencias().get_head()
        return  visitados

    def remove_repetidos(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l

    def verifica_repet(self,arr, v):
        if len(arr) > 2:
            arr = arr[len(arr) - 3:len(arr)]
            if arr[0] == arr[2] and arr[1] == v:
                return True
        return False
    def arvore_prim(self):
        inicio = self.vertices[0]
        vistado = []
        vistado.append(inicio.get_no().get_data())
        valor = 1000000
        t = inicio.get_adjacencias().get_head()
        g = None
        ferrados = []
        while len(self.remove_repetidos(vistado)) < len(self.vertices):
            while t != None:
                if t.get_peso() <= valor and self.verifica_repet(vistado, t.get_data()) == False and t.get_data() not in ferrados:
                    valor = t.get_peso()
                    g = self.get_vertice(t.get_data())
                if self.verifica_repet(vistado, t.get_data()) == True:
                    arr = vistado[len(vistado) - 3:len(vistado)]
                    ferrados.append(arr[0])
                    ferrados.append(t.get_data())
                t = t.get_next()
            valor = 1000000
            vistado.append(g.get_no().get_data())
            t = g.get_adjacencias().get_head()
            g = None
        return vistado

    def dkitra(self,vertice):
        inicio = self.vertices[0]
        vistado = []
        vistado.append(inicio.get_no().get_data())
        valor = 1000000
        t = inicio.get_adjacencias().get_head()

        return None


grafo = Grafo([])

a = vertice(No("V1", 0), lista())
a.add_adjacencia("V2", 1)
a.add_adjacencia("V5", 1)
grafo.add_aresta(a.get_no(), a.get_adjacencias())

a = vertice(No("V2", 0), lista())
a.add_adjacencia("V1", 1)
a.add_adjacencia("V4", 3)
a.add_adjacencia("V3", 4)
grafo.add_aresta(a.get_no(), a.get_adjacencias())

a = vertice(No("V3", 0), lista())
a.add_adjacencia("V2", 4)
a.add_adjacencia("V4", 1)
a.add_adjacencia("V5", 2)
grafo.add_aresta(a.get_no(), a.get_adjacencias())

a = vertice(No("V4", 0), lista())
a.add_adjacencia("V2", 3)
a.add_adjacencia("V3", 1)
a.add_adjacencia("V5", 3)
grafo.add_aresta(a.get_no(), a.get_adjacencias())

a = vertice(No("V5", 0), lista())
a.add_adjacencia("V1",   1)
a.add_adjacencia("V3", 2)
a.add_adjacencia("V4", 1)
grafo.add_aresta(a.get_no(), a.get_adjacencias())


#print(grafo.arvore_prim())
print(grafo.busca_profundidade("V1","V4"))
#print(grafo.busca_largura("V5"))
#print(grafo.dkitra("V3"))
