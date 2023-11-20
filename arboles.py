from pruebas import *
import matplotlib.pyplot as plt

class nodo_tree(object):
    #crea el objeto que tendrá cada uno de los nodos del árbol
    def __init__(self, nombre, padre, lado, hijo1, hijo2):
        self.nombre = nombre
        self.padre = padre
        self.lado = lado
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def pregunta(hijo1, hijo2):
        preferencias = f"""
                Indique su preferencia:
                1: {hijo1}
                2: {hijo2}
        """
        print(preferencias)

def main ():
    
    raiz = nodo_arbol(nodo_tree("viajes", None,None,"relajacion","no_relajacion"))
#\
    with open('estructura_arbol.txt', 'r') as archivo:
        lineas = archivo.readlines()
        listaYaPasados = []
        diccionario_arbol_grafica = {}
        for linea in lineas:
            variables = linea.split(",")

            #Diccionario Grafica
            if variables[1] in listaYaPasados:
                diccionario_arbol_grafica[variables[1]].append(variables[0])
            else:
                diccionario_arbol_grafica[variables[1]] = []
                diccionario_arbol_grafica[variables[1]].append(variables[0])
                listaYaPasados.append(variables[1])

            if variables[0] not in listaYaPasados:
                diccionario_arbol_grafica[variables[0]] = []

            #Arbol
            objeto1 = nodo_tree(variables[0],variables[1],int(variables[2]),variables[3],variables[4])
            insertar_nodo(raiz,objeto1)

    # por_nivel(raiz)
    print(raiz.info.nombre)
    print(diccionario_arbol_grafica)

    def plot_tree(tree, parent_name, graph, pos=None, level=0, width=50, vert_gap = 500, xcenter = 0.5):
        if pos is None:
            pos = {parent_name: (xcenter, 1 - level * vert_gap)}
        else:
            pos[parent_name] = (xcenter, 1 - level * vert_gap)
        neighbors = graph[parent_name]
        if len(neighbors) != 0:
            dx = width / 2 
            nextx = xcenter - width/2 - dx/2
            for neighbor in neighbors:
                nextx += dx
                pos = plot_tree(tree, neighbor, graph=graph, pos=pos,
                                level=level+1, width=dx, xcenter=nextx)
        return pos

    # Crear el gráfico
    pos = plot_tree(diccionario_arbol_grafica, 'viajes', diccionario_arbol_grafica)

    # Dibujar el gráfico
    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=300, color='white', edgecolors='black')
        plt.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), rotation = 45)

    for parent, children in diccionario_arbol_grafica.items():
        for child in children:
            plt.plot([pos[parent][0], pos[child][0]], [pos[parent][1], pos[child][1]], color='black')

    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=1, hspace=1)

    plt.show()
       
main() 
    
    
    


        