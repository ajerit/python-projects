# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
'''
Implementacion del TAD Indice : Tabla de Hash.
Usa encadenamiento con listas doblemente enlazadas para manejar colisiones
Cada indice es una tabla de hash con buckets. 
Cada bucket contiene un nodo con propiedades next, prev, string y lista. 
Lista es una ListaReproduccion con las canciones que fueron hasheadas a ese lugar
'''

from listarep import *
from dlist import *
from fnvhash import fnv1a_32


class Indice:
    # Inicializamos un objeto Indice, con numero de buckets opcional
    def __init__(self, m=5):
        self._size = 0 # cantidad de elementos
        self._buckets = [dList() for x in range(m)] # cantidad buckets = len(buckets)
    
    # Funcion fnv para hashear los strings
    def fnv(self, string):
        hashed  = fnv1a_32(string)
        
        # Evitamos valores fuera de la longitud de la tabla
        index = hashed % len(self._buckets)
        return index
    
    # Funcion para agregar elementos a la tabla    
    def agregar(self, stringKey, cancion):
        hashed = self.fnv(stringKey)
        dlist = self._buckets[hashed]
        
        pList = dlist.search(stringKey)
        # pList == None : stringKey no está en bucket
            
        if pList is not None: #Agregamos la cancion a la lista
            pList.agregar(cancion)
        else: 
            pList = ListaReproduccion()
            pList.agregar(cancion)
            dlist.add(stringKey, pList)
        
        self._size += 1
            
        # Rehashing
        fcarga = float(self._size) / float(len(self._buckets))
        if fcarga >= 0.8: 
            self.rehash()
    
    # Funcion para buscar elementos en la tabla  
    # Devuelve una listaReproduccion
    def buscar(self, stringKey):
        hashed = self.fnv(stringKey)
        curList = self._buckets[hashed]
        return curList.search(stringKey)
    
    # Funcion de rehashing para mantener una carga menor a 0.8    
    def rehash(self):
        mNuevo = 2*len(self._buckets) + 1
        newTable = Indice(mNuevo)
        # Agregar elementos actuales a la nueva tabla
        for bucket in self._buckets:
            #bucket es una dList
            curList = bucket.head
            for i in range(len(bucket)):
                curSong = curList._cont._head
                for j in range(len(curList._cont)):
                    newTable.agregar(curList._key, curSong.song)
                    curSong = curSong._next
                curList = curList._next

        # self es inmutable, entonces copiamos el array de buckets    
        self._buckets = newTable._buckets
