class nodoPila(object):
    info, sig = None, None

class pila(object):
    def __init__(self):
        self.tamanio = 0
        self.cima = None

    def push(pila,dato): #apilar: apila el dato sobre la cima de la pila
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.tamanio += 1

    def pop(pila): #desapilar: desapila el elemnto de la cima de la pila y lo devuelve
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x

    def __str__(self):
        nodo_actual = self.cima
        elementos = []
        while nodo_actual:
            elementos.append(nodo_actual.info)
            nodo_actual = nodo_actual.sig
        return str(elementos)
