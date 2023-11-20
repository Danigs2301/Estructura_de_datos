class nodoLista(object):
    info, sig = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamano = 0


def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato

    # se agrega el nuevo nodo al principio
    nodo.sig = lista.inicio
    lista.inicio = nodo

    lista.tamano += 1

def lista_vacia(lista):
    return lista.inicio is None

def eliminar(lista, clave):
    dato = None
    if(lista.inicio.info == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while(actual is not None and actual.info != clave):
            anterior = anterior.sig
            actual = actual.sig
        if(actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamano -= 1
    return dato

def tamano(lista):
    return lista.tamano

def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig