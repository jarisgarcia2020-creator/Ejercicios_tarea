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
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def sumar(self, nodo):
        if nodo is None:
            return 0
        return (nodo.valor + self.sumar(nodo.izquierdo)
                + self.sumar(nodo.derecho))


arbol = ArbolBinarioBusqueda()
for numero in [50, 30, 70, 80, 90]:
    arbol.insertar(numero)

print("Arbol Original: [50, 30, 70, 80, 90] ")
print("Suma:", arbol.sumar(arbol.raiz))
