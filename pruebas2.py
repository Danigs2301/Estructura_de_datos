def inorden (raiz, buscado):
    #Realiza el barrido inorden del árbol
    
    if(raiz is not None):
        raiz1 = raiz
        inorden(raiz.izq, buscado)
        if(raiz.info.nombre == buscado):
            raiz1 = raiz
        inorden(raiz.der, buscado)
        if(raiz.info.nombre == buscado):
            raiz1 = raiz
    
    return raiz1

class nodo_arbol(object):
    #Clase nodo árbol

    def __init__(self, info):
        #Crea un nodo con la información cargada 
        self.izq = None
        self.der = None
        self.info = info


def insertar_nodo(raiz, dato):
    #Insertar un dato al árbol

    raiz = inorden(raiz, dato.padre)
    if (dato.lado == 1):
        raiz.izq = nodo_arbol(dato) 
    elif (dato.lado == 2):
        raiz.der = nodo_arbol(dato)
    
    return raiz
