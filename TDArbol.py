from TDACola import *

class nodo_arbol(object):
    #Clase nodo árbol

    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
    

class ResultadoBusqueda:
    def __init__(self, nodo_encontrado=None):
        self.nodo_encontrado = nodo_encontrado


def eliminar_nodo(raiz, clave):
    #Elimina un elemento del árbol y lo devuelve si lo encuentra

    x = None
    if (raiz is not None):
        if (clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if (raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    
    return raiz, x

def arbol_vacio(raiz):
    #Devuelve true si el árbol está vacio
    return raiz is None

def remplazar(raiz):
    #Determina el nodo que reemplazará al que se elimina

    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else: 
        raiz.der, aux = remplazar(raiz.der)
    
    return raiz, aux

def por_nivel(raiz):
    #Realiza el barrido postorden del árbol

    pendientes = Cola()
    arribo(pendientes, raiz)

    while (not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info.nombre)
        if (nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)

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

def preorden(raiz):
    #Realiza el barrido preorden del árbol

    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    #Realiza el barrido postorden del árbol

    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def inorden(raiz, buscado):
    # Realiza el barrido inorden del árbol, busca un dato en especifico y devuelve la dirección de memoria 
    raiz1 = None 

    if raiz is not None:
        resultado_izq = inorden(raiz.izq, buscado)

        if resultado_izq.nodo_encontrado:
            return resultado_izq

        if raiz.info.nombre == buscado:
            return ResultadoBusqueda(raiz)
        
        resultado_der = inorden(raiz.der, buscado)

        if resultado_der.nodo_encontrado:
            return resultado_der

    return ResultadoBusqueda()



def insertar_nodo(raiz, dato):
    # Insertar un dato al árbol encontrando el padre y el lado donde desea colocar el nuevo nodo
    resultado_busqueda = inorden(raiz, dato.padre)

    if resultado_busqueda.nodo_encontrado:
        nodo_padre = resultado_busqueda.nodo_encontrado

        if dato.lado == 1:
            nodo_padre.izq = nodo_arbol(dato)
        elif dato.lado == 2:
            nodo_padre.der = nodo_arbol(dato)
    else:
        print(f"No se encontró el nodo padre {dato.padre}")

    return raiz