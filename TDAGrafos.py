# Ahora Python
from collections import deque
import math



class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    def imprimir_matriz(self, m, texto):
        cadena = ""

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " + ("   -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += "\t" + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += "\t" + "X"
                        else:
                            cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Redimensiono la matriz de adyacencia.
        # Para preparalarla para agregar más Aristas.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Recorro la matriz y copio su contenido dentro de la matriz más grande.
        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        # Igualo la matriz a la matriz más grande.
        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, valor, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        # Si estan contenidos en la lista de vertices.
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

        # Si la arista entrante no es dirijida.
        # Instancio una Arista en sentido contrario de Fin a Inicio.
        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

    def recorrido_anchura(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None

        recorrido = []
        cola = deque([inicio])

        while len(cola) > 0:
            v_aux = cola.popleft()
            recorrido.append(v_aux)

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]
                    if not self.contenido_en(recorrido, v_candidato) and not self.contenido_en(cola, v_candidato):
                        cola.append(v_candidato)

        return recorrido

    def recorrido_profundidad(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None

        recorrido = []
        pila = [inicio]

        while len(pila) > 0:
            v_aux = pila.pop()

            if not self.contenido_en(recorrido, v_aux):
                recorrido.append(v_aux)

            condicion = True

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]

                    # al parecer se puede reemplazar por "and not self.contenido_en(pila, v_candidato)
                    if not self.contenido_en(recorrido, v_candidato) and condicion:
                        # Es como un Break.
                        condicion = False

                        pila.append(v_aux)
                        pila.append(v_candidato)

        return recorrido

    def obtener_sucesores(self, v):
        pos_vertice = self.vertices.index(v)

        list_sucesores = []

        for i in range(len(self.matriz)):
            if self.matriz[pos_vertice][i] is not None:
                list_sucesores.append(self.vertices[i])

        return list_sucesores

    # Aciclico.
    def camino(self, k, v2):
        # Con ciclos.
        return self.__camino(k, v2, [])

    def __camino(self, k, v2, visitados):
        if k == v2:
            return True

        visitados.append(k)
        sucesores = self.obtener_sucesores(k)

        for vertice in sucesores:
            if not self.contenido_en(visitados, vertice):
                if self.__camino(vertice, v2, visitados):
                    return True

        return False

    #EL MÉTODO DE FLOYD WARSHALL devuelve dos matrices: floyd que contiene los caminos más cortos de un vertice a otro, y warshall, que contiene información para reconstruir los caminos.
    def floyd_warshall(self):
        filas = columnas = len(self.matriz)
        floyd = [[None] * filas for i in range(columnas)]
        warshall = [[None] * filas for i in range(columnas)]

        # Inicializo Floyd y Warshall.
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                # Warshall.
                warshall[f][c] = self.vertices[f]

                # Floyd.
                if f == c:
                    floyd[f][c] = 0
                else:
                    if self.matriz[f][c] is None:
                        # Instancio como infinito.
                        # para comprobar si es infinito se utiliza, math.isinf(float).
                        floyd[f][c] = float("inf")
                    else:
                        floyd[f][c] = self.matriz[f][c]

        # Ejecuto el algoritmo.
        for i in range(len(floyd)):
            for x in range(len(floyd)):
                for y in range(len(floyd)):
                    suma = floyd[i][x] + floyd[y][i]

                    if suma < floyd[y][x]:
                        floyd[y][x] = suma

                        # \x1b[4m "4 es un código numérico que indica que formato se le va a dar" \x1b[0m.
                        warshall[y][x] = "[" + self.vertices[i] + "]"

        return floyd, warshall

    def floyd_warshall2(self):
        filas = columnas = len(self.matriz)
        floyd = [[None] * filas for _ in range(columnas)]
        warshall = [[None] * filas for _ in range(columnas)]

        # Inicializo Floyd y Warshall.
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                # Warshall.
                warshall[f][c] = None  # Inicializar predecesores como None.

                # Floyd.
                if f == c:
                    floyd[f][c] = 0
                else:
                    if self.matriz[f][c] is None:
                        # Instancio como infinito.
                        floyd[f][c] = float("inf")
                    else:
                        floyd[f][c] = self.matriz[f][c]

        # Ejecuto el algoritmo.
        for k in range(len(floyd)):
            for i in range(len(floyd)):
                for j in range(len(floyd)):
                    suma = floyd[i][k] + floyd[k][j]

                    if suma < floyd[i][j]:
                        floyd[i][j] = suma
                        warshall[i][j] = self.vertices[k]  # Actualizar predecesor.

        return floyd, warshall