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
            self._insertar_recursivo(self.raiz, valor)s

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)

        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def inorden(self):
        lista = []
        self._inorden_recursivo(self.raiz, lista)
        return lista

    def _inorden_recursivo(self, nodo, lista):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, lista)

    def balancear_arbol(self):
        datos = self.inorden()
        arbol_nuevo = ArbolBinarioBusqueda()

        arbol_nuevo.raiz = self._crear_arbol(
            datos, 0, len(datos) - 1
        )

        return arbol_nuevo

    def _crear_arbol(self, datos, inicio, fin):
        if inicio > fin:
            return None

        medio = (inicio + fin) // 2
        nodo = NodoArbol(datos[medio])

        nodo.izquierdo = self._crear_arbol(
            datos, inicio, medio - 1
        )

        nodo.derecho = self._crear_arbol(
            datos, medio + 1, fin
        )

        return nodo

    def altura(self, nodo):
        if nodo is None:
            return -1

        izquierda = self.altura(nodo.izquierdo)
        derecha = self.altura(nodo.derecho)

        return 1 + max(izquierda, derecha)


# Arbol inicial
arbol = ArbolBinarioBusqueda()

for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    arbol.insertar(numero)

print("Altura del árbol inicial:", arbol.altura(arbol.raiz))

# Balance
arbol_nuevo = arbol.balancear_arbol()

print("Altura del árbol nuevo:", arbol_nuevo.altura(
    arbol_nuevo.raiz
))

print("Números del árbol inicial:", arbol.inorden())
print("Números del árbol balanceado:", arbol_nuevo.inorden())
