# Hashtable implementation with chaining using doubly linked lists
# Implementacion de Tablas de Hash con encadenamiento
# Adolfo Jeritson. 12-10523
# 2016

from dlist import *

class HashTable:
    # Metodo que construye nuevo HT al instanciar
    def __init__(self, n):
        self._size = n
        self._arr = [dList() for x in range(n)]
    
    # Metodo para devolver la longitud    
    def __len__(self):
        return self._size
    
    # Metodo para verificar si algun elemento esta en la tabla
    def __contains__(self, target):
        for i in range(self._size):
            exists = target in self._arr[i]
            if exists:
                return exists
            
    # Funcion de hash, metodo multiplicativo recomendado por Knuth
    def h(self, k):
        return int(self._size*((k*0.180339887) % 1))
    
    # Metodo para agregar a la tabla segun HashEntry
    def addEntryHash(self, entry):
        hashed = self.h(entry.key)
        dlist = self._arr[hashed]
        
        if entry.key in dlist:
            dlist.remove(entry.key)
            
        entry.next = dlist._head
        
        if dlist._head is not None:
            dlist._head.prev = entry
            
        dlist._head = entry
        dlist._size += 1
    
    # Metodo para agregar a la tabla segun key y string
    def addHashtable(self, key, st):
        hashed = self.h(key)
        dlist = self._arr[hashed]
        if key in dlist:
            dlist.remove(key)
        dlist.add(key, st)
    
    # Metodo para eliminar de la tabla segun HashEntry
    def removeEntryHash(self, entry):
        hashed = self.h(entry.key)
        dlist = self._arr[hashed]
        return dlist.remove(entry.key)
    
    # Metodo para eliminar de la tabla segun key    
    def removeHashtable(self, key):
        hashed = self.h(key)
        curList = self._arr[hashed]
        return curList.remove(key)
    
    # Metodo para buscar un key en la tabla y retornar el string
    def searchHashtable(self, key):
        hashed = self.h(key)
        return self._arr[hashed].search(key)
    
    # Metodo que muetra todos los elementos en la tabla
    def showHashtable(self):
        for i in range(self._size):
            self._arr[i].showList()
        
