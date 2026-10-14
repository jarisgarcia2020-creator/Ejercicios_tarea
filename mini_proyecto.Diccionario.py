# Mini_proyecto: Diccionario_Inteligente
# Estructura_de_datos: Arbol_Binario_de_Busqueda

class Palabra:
    def __init__(self, texto, definicion):
        self.texto = texto
        self.definicion = definicion

class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = Nodo(palabra)
        else:
            self._insertar_recursivo(self.raiz, palabra)

    def _insertar_recursivo(self, nodo, palabra):
        actual = nodo.palabra.texto.casefold()
        nuevo = palabra.texto.casefold()

        if nuevo < actual:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabra)

        elif nuevo > actual:
            if nodo.derecho is None:
                nodo.derecho = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.derecho, palabra)

    def buscar(self, texto):
        return self._buscar_recursivo(self.raiz, texto.casefold())

    def _buscar_recursivo(self, nodo, texto):
        if nodo is None:
            return None

        actual = nodo.palabra.texto.casefold()

        if texto == actual:
            return nodo.palabra
        elif texto < actual:
            return self._buscar_recursivo(nodo.izquierdo, texto)
        else:
            return self._buscar_recursivo(nodo.derecho, texto)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.palabra)
            self._inorden_recursivo(nodo.derecho, resultado)

    def buscar_por_prefijo(self, prefijo):
        palabras = self.inorden()
        resultado = []

        for palabra in palabras:
            if palabra.texto.casefold().startswith(prefijo.casefold()):
                resultado.append(palabra)

        return resultado

def cargar_diccionario(arbol):
    for texto, definicion in datos:
        palabra = Palabra(texto, definicion)
        arbol.insertar(palabra)

# Diccionario con 50 palabras y definiciones   
datos = [
    ("algoritmo", "Pasos ordenados para solucionar un problema."),
    ("almacenamiento", "Proceso de guardar datos para utilizarlos despues."),
    ("analisis", "Examen de datos para comprender una situacion."),
    ("aplicacion", "Programa creado para realizar una tarea especifica."),
    ("archivo", "Unidad que contiene informacion almacenada."),
    ("arbol", "Estructura de datos formada por nodos relacionados."),
    ("arreglo", "Conjunto de elementos almacenados en una coleccion."),
    ("atributo", "Propiedad que describe un objeto."),
    ("autenticacion", "Verificacion de la identidad de un usuario."),
    ("autocompletar", "Funcion que sugiere palabras mientras se escribe."),
    ("automatizacion", "Uso de tecnologia para ejecutar tareas automaticamente."),
    ("backup", "Copia de seguridad de informacion importante."),
    ("base de datos", "Conjunto organizado de datos relacionados."),
    ("binario", "Sistema numerico que utiliza cero y uno."),
    ("bit", "Unidad minima de informacion digital."),
    ("booleano", "Tipo de dato que representa verdadero o falso."),
    ("buscador", "Herramienta para localizar informacion en internet."),
    ("byte", "Unidad digital equivalente a ocho bits."),
    ("cable", "Medio fisico que transmite energia o datos."),
    ("cache", "Memoria temporal que agiliza el acceso a datos."),
    ("cadena", "Secuencia de caracteres que representa texto."),
    ("captcha", "Prueba que ayuda a distinguir personas de programas."),
    ("ciberseguridad", "Proteccion de sistemas y datos frente a ataques."),
    ("circuito", "Conjunto de componentes conectados electronicamente."),
    ("cliente", "Equipo o programa que solicita un servicio."),
    ("codigo fuente", "Instrucciones escritas por un programador."),
    ("compilador", "Programa que traduce codigo a otro formato ejecutable."),
    ("computadora", "Maquina electronica que procesa informacion."),
    ("conectividad", "Capacidad de establecer conexiones entre dispositivos."),
    ("contraseña", "Clave secreta utilizada para acceder a una cuenta."),
    ("cookie", "Dato que un sitio web guarda en el navegador."),
    ("cursor", "Indicador que muestra la posicion de escritura o seleccion."),
    ("dato", "Representacion de un valor o hecho."),
    ("diccionario", "Estructura que relaciona claves con valores."),
    ("direccion IP", "Numero que identifica un dispositivo en una red."),
    ("disco duro", "Dispositivo utilizado para guardar informacion."),
    ("dominio", "Nombre que identifica un sitio en internet."),
    ("encriptacion", "Transformacion de datos para proteger su contenido."),
    ("ensamblador", "Programa que traduce instrucciones de ensamblador."),
    ("entrada", "Informacion que recibe un programa."),
    ("escaner", "Dispositivo que digitaliza documentos o imagenes."),
    ("etiqueta", "Marca utilizada para identificar o clasificar elementos."),
    ("firewall", "Sistema que controla el trafico de una red."),
    ("formateo", "Preparacion de un medio de almacenamiento para su uso."),
    ("funcion", "Bloque de codigo que realiza una tarea concreta."),
    ("hardware", "Componentes fisicos de una computadora."),
    ("hipervinculo", "Enlace que dirige a otro recurso digital."),
    ("hosting", "Servicio que permite alojar sitios web."),
    ("html", "Lenguaje utilizado para estructurar paginas web."),
    ("interfaz", "Medio por el que el usuario interactua con un sistema.")
]

def mostrar_menu():
    """Presenta las opciones de menú"""
    print("\n===== DICCIONARIO INTELIGENTE =====")
    print("1. Buscar palabra")
    print("2. Autocompletar por prefijo")
    print("3. Mostrar diccionario completo")
    print("4. Salir")


def ejecutar_programa():
    """Controla la ejecucion del programa."""
    arbol = ArbolBinarioBusqueda()
    cargar_diccionario(arbol)

    print("Diccionario cargado correctamente.")
    print("Cantidad de palabras:", len(arbol.inorden()))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            texto = input("Escriba la palabra: ").strip()
            resultado = arbol.buscar(texto)

            if resultado is not None:
                print("\nPalabra:", resultado.texto)
                print("Definicion:", resultado.definicion)
            else:
                print("La palabra no se encuentra en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escriba el prefijo: ").strip()

            if not prefijo:
                print("Debe escribir un prefijo.")
                continue

            resultados = arbol.buscar_por_prefijo(prefijo)

            if resultados:
                print("\nPalabras encontradas:")
                for palabra in resultados:
                    print("-", palabra.texto, ":", palabra.definicion)
            else:
                print("No hay palabras con ese prefijo.")

        elif opcion == "3":
            print("\n===== DICCIONARIO COMPLETO =====")

            for palabra in arbol.inorden():
                print(palabra.texto, ":", palabra.definicion)

        elif opcion == "4":
            print("Gracias por usar el Diccionario Inteligente.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_programa()
