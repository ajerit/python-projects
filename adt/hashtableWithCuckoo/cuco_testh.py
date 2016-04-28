
# Client para probar las listas enlazadas y tablas de hash
# Marzo 2016

import sys, traceback, random, time
from cuco_htable import *

class NoPasaElTest(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        
def revisarSize(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("Esta calculando mal el size")
        
def revisarContains(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("El metodo __contains__ no esta funcionando correctamente")

def revisarAddHash(tabla,key,st):
    tabla.addCucoHash(key,st)
    if not key in tabla:
        raise NoPasaElTest("El metodo .addHashtable (key) no esta funcionando correctamente")
        
def revisarRemoveHash(tabla, key):
    busq = tabla.searchHashtable(key)
    elim = tabla.removeHashtable(key)
    if busq != elim:
        raise NoPasaElTest("El metodo .removeHashtable no esta funcionando correctamente")

def probarHash():
    ht = CucoTable(50)
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
        revisarAddHash(ht, 2,'two')
        print("Se verifico que el metodo .addEntryHash funciona cuando la tabla tiene cosas")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
       
        revisarAddHash(ht, 3,'three')
        print("Se verifico que el metodo .addEntryHash funciona cuando la tabla tiene cosas")
    except NoPasaElTest as e:
        print(e.mensaje)
    
    try:
        revisarContains(0 in ht,False)
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

        revisarAddHash(ht,3,'three new')
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
        

        
################################
## Inicio de la Aplicacion
################################

if __name__ == "__main__":
    print("------- PROBANDO HASHTABLE -------")
    probarHash()
