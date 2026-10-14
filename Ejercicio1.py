class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return NodoArbol(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar(nodo.derecho, valor)
        return nodo

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    def eliminar(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo

            sucesor = nodo.derecho
            while sucesor.izquierdo:
                sucesor = sucesor.izquierdo
            nodo.valor = sucesor.valor
            nodo.derecho = self.eliminar(
                nodo.derecho, sucesor.valor)
        return nodo


arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Antes de eliminar: 80")
arbol.inorden(arbol.raiz)

arbol.raiz = arbol.eliminar(arbol.raiz, 80)

print("\nDespués de eliminar:80")
arbol.inorden(arbol.raiz)
print()

print()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Antes de eliminar: 70")
arbol.inorden(arbol.raiz)

arbol.raiz = arbol.eliminar(arbol.raiz, 70)

print("\nDespués de eliminar:70")
arbol.inorden(arbol.raiz)
print()

print()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Antes de eliminar: 50")
arbol.inorden(arbol.raiz)

arbol.raiz = arbol.eliminar(arbol.raiz, 50)

print("\nDespués de eliminar:50")
arbol.inorden(arbol.raiz)
print()
