
# Client para probar las listas enlazadas y tablas de hash
# Marzo 2016

import sys, traceback, random, time
from hashtable import *

class NoPasaElTest(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        
def revisarSize(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("Esta calculando mal el size")
        
def revisarContains(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("El metodo __contains__ no esta funcionando correctamente")

def revisarAdd(lista,key,st):
    l = []
    for i in lista:
       l.append(i)
    l.append(key)
    lista.add(key, st)
    for i in l:
       if  not i in lista:
          raise NoPasaElTest("El metodo .add no esta funcionando correctamente")
          
def revisarRemove(lista,elem):
    l = []
    for i in lista:
       l.append(i)
    l.remove(elem)
    lista.remove(elem)
    for i in l:
       if not i in lista:
          raise NoPasaElTest("El metodo .remove no esta funcionando correctamente")

def revisarAddHash(tabla,key,st):
    tabla.addHashtable(key,st)
    if not key in tabla:
        raise NoPasaElTest("El metodo .addHashtable (key) no esta funcionando correctamente")
    elif not st in tabla:
        raise NoPasaElTest("El metodo .addHashtable (str) no esta funcionando correctamente")
        
def revisarAddHashEntry(tabla, entry):
    key = entry.key
    st = entry.string
    tabla.addEntryHash(entry)
    if not key in tabla:
        raise NoPasaElTest("El metodo .addEntryHash (key) no esta funcionando correctamente")
    elif not st in tabla:
        raise NoPasaElTest("El metodo .addEntryHash (str) no esta funcionando correctamente")

def revisarRemoveHash(tabla, key):
    hashed = tabla.h(key)
    busq = tabla.searchHashtable(key)
    elim = tabla.removeHashtable(key)
    if busq != elim:
        raise NoPasaElTest("El metodo .removeHashtable no esta funcionando correctamente")

def revisarRemoveEntryHash(tabla, entry):
    hashed = tabla.h(entry.key)
    busq = tabla.searchHashtable(entry.key)
    elim = tabla.removeHashtable(entry.key)
    if busq != elim:
        raise NoPasaElTest("El metodo .removeEntryHash no esta funcionando correctamente")

def probarHash():
    ht = HashTable(50)
    try:
        revisarSize(len(ht),50)
        print("Se verifico 'LEN()' para tabla hash vacia")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        revisarContains(1 in ht,False)
        print("Se verifico que la operacion 'in' funciona para tabla vacia")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        revisarAddHash(ht, 0, 'cero')
        print("Se verifico que el metodo .addHashtable funciona cuando la tabla es vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        newEntry = HashEntry(2,'two')
        revisarAddHashEntry(ht, newEntry)
        print("Se verifico que el metodo .addEntryHash funciona cuando la tabla tiene cosas")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        newEntry = HashEntry(3,'three')
        revisarAddHashEntry(ht, newEntry)
        print("Se verifico que el metodo .addEntryHash funciona cuando la tabla tiene cosas")
    except NoPasaElTest as e:
        print(e.mensaje)
    
    try:
        revisarContains(0 in ht,True)
        print("Se verifico que la operacion 'in' funciona")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(ht),50)
        print("Se verifico el calclulo de longitud")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        revisarRemoveHash(ht,0)
        print("Se verifico que el metodo .removeHashtable funciona")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        remEntry = HashEntry(2,'two')
        revisarRemoveEntryHash(ht,remEntry)
        print("Se verifico que el metodo .removeHashEntry funciona")
    except NoPasaElTest as e:
        print(e.mensaje)
    
    try:
        newEntry = HashEntry(3,'three new')
        revisarAddHashEntry(ht, newEntry)
        print("Se verifico que el metodo .addEntryHash funciona cuando ya existe el key")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        print("")
        print("KEY | STRING")
        print("------------")
        ht.showHashtable()
        print("")
    except NoPasaElTest as e:
        print(e.mensaje)
        

def probarDList():
    dl = dList()
    try:
        revisarSize(len(dl),0)
        print("Se verifico 'LEN()' para lista vacia")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        revisarContains(1 in dl,False)
        print("Se verifico que la operacion 'in' funciona para lista vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(dl,0,'cero')
        print("Se verifico que el metodo add funciona cuando la lista es vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarContains(0 in dl,True)
        print("Se verifico que la operacion 'in' funciona para lista de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(dl),1)
        print("Se verifico el calclulo de longitud para lista con un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(dl,1,'uno')
        print("Se verifico que el metodo add funciona cuando la lista tiene un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        revisarContains('uno' in dl,True)
        print("Se verifico que la operacion 'in' funciona para lista con mas de un elemento y strings")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    try:
        print("")
        print("KEY | STRING")
        print("------------")
        dl.showList()
        print("")
    except NoPasaElTest as e:
        print("Error al mostrar elementos de la lista")

    try:
        revisarContains(1 in dl,True)
        print("Se verifico que la operacion 'in' funciona para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(dl),2)
        print("Se verifico el calclulo de longitud para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarRemove(dl,1)
        print("Se verifico que el metodo remove funciona para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarRemove(dl,0)
        print("Se verifico que el metodo remove funciona para lista de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
        
        
################################
## Inicio de la Aplicacion
################################

if __name__ == "__main__":
    probarDList()
    print("------- PROBANDO HASHTABLE -------")
    probarHash()
