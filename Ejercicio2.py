from collections import deque

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            nodo = self.raiz
            while True:
                if valor < nodo.valor:
                    if nodo.izquierdo is None:
                        nodo.izquierdo = NodoArbol(valor)
                        break
                    nodo = nodo.izquierdo
                elif valor > nodo.valor:
                    if nodo.derecho is None:
                        nodo.derecho = NodoArbol(valor)
                        break
                    nodo = nodo.derecho
                else:
                    break

    def niveles(self):
        if self.raiz is None:
            return []

        cola = deque([self.raiz])
        resultado = []

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)

            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

        return resultado


arbol = ArbolBinarioBusqueda()
for x in [50, 30, 70, 20, 40]:
    arbol.insertar(x)

print("Recorrido:", arbol.niveles())
