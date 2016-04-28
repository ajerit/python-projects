# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# Implementacion de listas doblemente enlazadas para la tabla de hash
# en la clase Indice


# Nodo de la lista que representa el par Clave/Lista
class NodeEntry(object):
    def __init__(self, string, lista):
        self._next = None
        self._prev = None
        self._key = string
        self._cont = lista


class dList:
    # Constructor inicial, el head es none y size cero
    def __init__(self):
        self.head = None
        self._size = 0
        
    # Definimos metodo para retornar size
    def __len__(self):
        return self._size
        
    #Definimos metodo para usar sintaxis x in dList
    def __contains__(self, string):
        curNode = self.head
        for i in range(self._size):
            if curNode._key == string: 
                return True
            curNode = curNode._next
        return False
    
    # Metodo para agregar nuevos elementos a la lista doblemente enlazada
    def add(self, string, lista):
        newNode = NodeEntry(string, lista)
        
        if self.head is None:
            self.head = newNode
            self.head._next = newNode
            self.head._prev = newNode
        else:
            newNode._next = self.head
            newNode._prev = self.head._prev
            self.head._prev._next = newNode
            self.head._prev = newNode
            self.head = newNode

        self._size += 1

    # Metodo para buscar elementos en la lista
    def search(self, string):
        curNode = self.head
        for i in range(self._size):
            if curNode._key == string: 
                return curNode._cont
            curNode = curNode._next
        return None

    # Metodo para iterar en la lista
    def __iter__(self):
        return ListIterator(self.head)
        
        
# Clase iteradora para la lista
class ListIterator:
    def __init__(self,listHead):
        self._curNode = listHead

    def __iter__(self):
        return self
        
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode
            self._curNode = self._curNode._next
            return item

