# Adolfo Jeritson
# Hashtable implementation with universal hashing to solve collisions
# Marzo 2016
#

import random
from dlist import *

class HashTable:
    # Metodo que construye nuevo HT al instanciar
    def __init__(self, n):
        self._size = n
        self._arr = [dList() for x in range(n)]
        self._p = 7919
        self._a = random.randint(1,self._p - 1)
        self._b = random.randint(0,self._p - 1)
    
    # Metodo para devolver la longitud    
    def __len__(self):
        return self._size
    
    # Metodo para verificar si algun elemento esta en la tabla
    def __contains__(self, target):
        for i in range(self._size):
            exists = target in self._arr[i]
            if exists:
                return exists
            
    # Funcion de hash, metodo universal algebraico
    def h(self, k):
        return ((((self._a * k) + self._b) % self._p) % self._size)
    
    # Metodo para agregar a la tabla segun HashEntry
    def addEntryHash(self, entry):
        if entry.key > self._p:
            print("Error. La clave es muy grande.")
        else:
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
        if key > self._p:
            print("Error. La clave es muy grande.")
        else:
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
        
