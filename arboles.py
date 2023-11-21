from TDArbol import *
import matplotlib.pyplot as plt

class nodo_tree(object):
    #crea el objeto que tendrá cada uno de los nodos del árbol
    def __init__(self, nombre, padre, lado, hijo1, hijo2):
        self.nombre = nombre
        self.padre = padre
        self.lado = lado
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    #Pregunta acerca de la preferencia que desea seleccionar el usuario de acuerdo al árbol 
    def pregunta(self, padre, hijo1, hijo2):
        preferencias = f"""
                Indique su preferencia:
                1: {hijo1}
                2: {hijo2}
        """
        print(preferencias)

#Realiza el recorrido del árbol dependiendo de hacia que lado se dirigen las preferencias del usuario
def recorrer(raiz, lado):
    if lado == 1:
        raiz=raiz.izq

    elif lado == 2:
        raiz = raiz.der
    
    return raiz

#Solicita la información acerca de la preferencia que desea el usuario, imprimiendo las preferencias 
def recorrer_arbol(raiz):
    while True:
        raiz.info.pregunta(raiz.info.nombre, raiz.info.hijo1, raiz.info.hijo2)
        
        while True:
            try:
                lado = int(input("Ingrese la opción de preferencia (1 o 2): "))
                if lado in (1, 2):
                
                    break
                else:
                    print("Error: Por favor, ingrese un número válido (1 o 2).")
            except ValueError:
                print("Error: Por favor, ingrese un número entero.")

        raiz = recorrer(raiz, lado)
        
        if raiz.izq == None or raiz.der == None:
            print(raiz.info.nombre)
            break  


#Base de código del archivo donde se crea la raiz, se lee el archivo txt con la estructura del árbol y gráfica el árbol 
def ejecucion_arbol ():
    
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
    recorrer_arbol(raiz)