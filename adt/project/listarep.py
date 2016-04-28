# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# Implementacion del TAD ListaReproduccion con listas doblemente 
# enlazadas circulares
import sys

# Clase iteradora
class ListIterator:
    def __init__(self,listHead):
        self._listRef = listHead._prev
        self._curNode = self._listRef
        self._done = self._listRef is None

    def __iter__(self):
        return self
        
    def next(self):
        if self._done:
            raise StopIteration
        else:
            self._curNode = self._curNode._next
            self._done = self._curNode is self._listRef
            return self._curNode.song


# Clase para los nodos de la lista
class ListRepNode(object):
    def __init__(self,song):
        self.song = song
        self._next = None
        self._prev = None


class ListaReproduccion:
    # Inicializa una lista de reproduccion vacia
    def __init__(self):
        self._head = None
        self._size = 0
        
    # Definimos metodo para retornar longitud
    def __len__(self):
        return self._size
        
    # Definimos metodo para usar sintaxis 'x in ListaReproduccion'
    def __contains__(self, cancion):
        curNode = self._head
        for i in range(self._size):
            if curNode.song.es_igual(cancion):
                return True
            curNode = curNode._next
        return False
    
    # Metodo para iterar en la lista
    def __iter__(self):
        return ListIterator(self._head)

    # Metodo para mostrar los elementos en la lista
    # Devuelve un arreglo de las canciones contenidas
    def mostrar(self):
        curList = []
        print("")
        print("LISTA DE CANCIONES".center(80))
        print("")
        print("%-28s %-31s %-21s" % ('Titulo', 'Artista', 'Genero'))
        print("%-28s %-31s %-21s" % ('-'*28, '-'*31, '-'*21))
        curNode = self._head
        for i in range(len(self)):
            print("%-28s %-31s %-21s" % (curNode.song.titulo, curNode.song.artista, curNode.song.genero))
            curList.append(curNode.song)
            curNode = curNode._next
        return curList
        
    # Metodo para agregar nueva cancion a la lista de reproduccion
    def agregar(self, cancion):
        newNode = ListRepNode(cancion)
        
        if self._head is None:
            self._head = newNode
            self._head._next = newNode
            self._head._prev = newNode
        else:
            newNode._next = self._head
            newNode._prev = self._head._prev
            self._head._prev._next = newNode
            self._head._prev = newNode
            self._head = newNode
            
        self._size += 1
    
    # Metodo para eliminar una cancion de la lista de reproduccion
    def eliminar(self, cancion):
        
        # Si la lista esta vacia, no se elimina nada.
        if len(self) > 0:
            curNode = self._head
            for i in range(len(self)):
                if curNode.song.es_igual(cancion):
                    b = curNode.song.es_igual(self._head.song)
                    if len(self) == 1:  # Caso de una sola cancion
                        self._head = None
                        self._size -= 1
                        return
                    else:               # Caso más de una canción
                        # Eliminamos la cancion (nodo) al encontrarlo
                        if b: self._head = curNode._next
                        curNode._prev._next = curNode._next
                        curNode._next._prev  = curNode._prev
                        self._size -= 1
                        return
                curNode = curNode._next
    
    # Metodo para realizar el ordenamiento de la lista
    def ordenar(self, type):
        sys.setrecursionlimit(len(self) +100)
        if self._size > 1:
            self._head._prev._next = None
            self._head._prev = None

            self._head = mergeSort(self._head, type)

            # Pegar finales
            curNode = self._head
            while curNode is not None and curNode._next is not None:
                curNode = curNode._next
            curNode._next = self._head
            self._head._prev = curNode

    def ordenar_titulo(self):
        self.ordenar(1)
        
    def ordenar_artista(self):
        self.ordenar(2)
        
        
# Funciones de ordenamiento
# Reciben la cabeza de la lista que van a ordenar
def mergeSort(head, orderType):
    if head is None or head._next is None:
        return head # Lista de cero o un elementos
    middle = split(head) # Divide lista en dos, cortando un ._next

    head = mergeSort(head,orderType)     # Ordena lista encabezada por head
                                         # ( lista: [head,middle)  )
    middle = mergeSort(middle,orderType) # Ordena lista encabezada por middle
                                         # y actualiza middle como cabeza de lista
    return merge(head, middle, orderType) # Mezcla ambas listas ordenadas

def split(head):
    fast = head
    slow = head
    while fast._next is not None and fast._next._next is not None:
        fast = fast._next._next
        slow = slow._next
    half = slow._next
    slow._next = None
    return half
    
def merge(a, b, orderType):
    if a is None: return b
    if b is None: return a
    
    if (orderType==1 and a.song.esmenor_titulo(b.song)) or (orderType==2 and a.song.esmenor_artista(b.song)):
        a._next = merge(a._next, b,orderType)
        a._next._prev = a
        a._prev = None
        return a
    else:
        b._next = merge(a, b._next,orderType)
        b._next._prev = b
        b._prev = None
        return b
            
        
