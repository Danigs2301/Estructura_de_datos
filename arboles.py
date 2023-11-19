from pruebas import *

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
    with open('proyecto_final\estructura_arbol.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            variables = linea.split(",")
            print(variables[0])
            objeto1 = nodo_tree(variables[0],variables[1],int(variables[2]),variables[3],variables[4])
            insertar_nodo(raiz,objeto1)

    por_nivel(raiz)

            
main()
    
    
    


        