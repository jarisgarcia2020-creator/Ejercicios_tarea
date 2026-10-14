class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def es_completo(self):
        def revisar(nodo):
            if nodo is None:
                return True

            if (nodo.izquierdo is None) != (
                    nodo.derecho is None):
                return False

            return (revisar(nodo.izquierdo)
                    and revisar(nodo.derecho))

        return revisar(self.raiz)


arbol = ArbolBinarioBusqueda()
arbol.raiz = NodoArbol(50)
arbol.raiz.izquierdo = NodoArbol(30)
arbol.raiz.derecho = NodoArbol(70)

print(arbol.es_completo())

arbol = ArbolBinarioBusqueda()
arbol.raiz = NodoArbol(50)
arbol.raiz.izquierdo = NodoArbol(30)

print(arbol.es_completo())
