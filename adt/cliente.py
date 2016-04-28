#!/usr/bin/env python

# Descripcion: Cliente que prueba los tipos concretos de
#     	       lista enlazada, cola y pila
# Autor: Federico Flaviani
# email: federico.flaviani@gmail.com

import sys, traceback, random, time
from linkedList import *
from stack import *
from queue import *

# Descripcion: Clase que implementa la exepcion que ocurre al momento que algun test no
#              pase la prueba

class NoPasaElTest(Exception):
      def __init__(self,mensaje):
          self.mensaje = mensaje

# Descripcion: funcion que hace testing del metodo __len__ de una lista
#   Atributos: valorActual: valor que devuelve len(lista) para la lista de prueba
#                 esperado: valor correcto para aprobar la prueba

def revisarSize(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("esta calculando mal la longitud")

# Descripcion: funcion que hace testing del metodo __contains__ de una lista
#   Atributos: valorActual: valor que devuelve (i in lista) para la lista de prueba
#                 esperado: valor correcto para aprobar la prueba

def revisarContains(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("el metodo __contains__ no esta funcionando correctamente")

#  Descripcion: funcion que hace testing del metodo add de una lista
#    Atributos: lista: lista de prueba para verificar su metodo add
#                elem: elemento a agregar a la lista

def revisarAdd(lista,elem):
    l = []
    for i in lista:
       l.append(i)
    l.append(elem)
    lista.add(elem)
    for i in l:
       if  not i in lista:
          raise NoPasaElTest("el metodo add no esta funcionando correctamente")

# asumimos que no hay repetidos
#  Descripcion: funcion que hace testing del metodo remove de una lista
#    Atributos: lista: lista de prueba para verificar su metodo remove
#                elem: elemento a eliminar de la lista

def revisarRemove(lista,elem):
    l = []
    for i in lista:
       l.append(i)
    l.remove(elem)
    lista.remove(elem)
    for i in l:
       if not i in lista:
          raise NoPasaElTest("el metodo remove no esta funcionando correctamente")

#  Descripcion: funcion que hace testing del metodo push de una pila
#    Atributos: pila: pila de prueba para verificar su metodo push
#               elem: elemento a empilar a la pila

def revisarPush(pila,elem):
    l = []
    for i in pila:
       l.append(i)
    l.append(elem)
    pila.push(elem)
    for i in l:
       if  not i in pila:
          raise NoPasaElTest("el metodo push no esta funcionando correctamente")
    if pila._top.data != elem:
          raise NoPasaElTest("el metodo push no esta funcionando correctamente")

#  Descripcion: funcion que hace testing del metodo push de una pila
#    Atributos: pila: pila de prueba para verificar su metodo push
#               elem: elemento a empilar a la pila
# Precondicion: Se asume que la pila no tiene elementos repetidos

def revisarPop(pila):
    l = []
    elem = pila._top.data
    for i in pila:
       l.append(i)
    l.pop()
    pila.pop()
    for i in l:
       if not i in pila:
          raise NoPasaElTest("el metodo pop no esta funcionando correctamente")

#  Descripcion: funcion que hace testing del metodo isEmpty de una cola
#    Atributos: cola: cola de prueba para verificar su metodo isEmpty

def revisarIsEmpty(cola):
    l = []
    for i in cola:
       l.append(i)
    if l != []:
       raise NoPasaElTest("el metodo isEmpty no esta funcionando correctamente")

def revisarEnqueue(cola,elem):
    l = []
    for i in cola:
       l.append(i)
    l.append(elem)
    cola.enqueue(elem)
    for i in l:
       if  not i in cola:
          raise NoPasaElTest("el metodo enqueue no esta funcionando correctamente")
    if cola._qtail.data != elem:
          raise NoPasaElTest("el metodo enqueue no esta funcionando correctamente")

def revisarDequeue(cola):
    l = []
    elem = cola._qhead.data
    for i in cola:
       l.append(i)
    l.reverse()
    l.pop()
    cola.dequeue()
    for i in l:
       if not i in cola:
          raise NoPasaElTest("el metodo dequeue no esta funcionando correctamente")

# Descripcion: Prueba los TADs Lista, Pila y Cola.
#
# Parametros: datos: arreglo con elementos de tipo numerico

def probarTADLista():
  
    l = LinkedList()
    try:
        print("Probando TAD Lista\n")
        revisarSize(len(l),0)
        print("Se verifico el calclulo de longitud para lista vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarContains(1 in l,False)
        print("Se verifico que la operacion 'in' funciona para lista vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(l,0)
        print("Se verifico que el metodo add funciona cuando la lista es vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarContains(0 in l,True)
        print("Se verifico que la operacion 'in' funciona para lista de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(l),1)
        print("Se verifico el calclulo de longitud para lista con un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(l,1)
        print("Se verifico que el metodo add funciona cuando la lista tiene un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarContains(1 in l,True)
        print("Se verifico que la operacion 'in' funciona para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(l),2)
        print("Se verifico el calclulo de longitud para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarRemove(l,1)
        print("Se verifico que el metodo remove funciona para lista con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarRemove(l,0)
        print("Se verifico que el metodo remove funciona para lista de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

def probarTADPila():
  
    p = Stack()
    try:
        print("Probando TAD Pila\n")
        revisarSize(len(p),0)
        print("Se verifico el calclulo de longitud para pila vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarPush(p,0)
        print("Se verifico que el metodo push funciona cuando la pila es vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(p),1)
        print("Se verifico el calclulo de longitud para pila con un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarPush(p,1)
        print("Se verifico que el metodo push funciona cuando la pila tiene un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(p),2)
        print("Se verifico el calclulo de longitud para pila con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarPop(p)
        print("Se verifico que el metodo pop funciona para pila con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
    except IndexError as e2:
        print("Mal implementado el metodo pop")

    try:
        revisarPop(p)
        print("Se verifico que el metodo pop funciona para pila de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
    except IndexError as e2:
        print("Mal implementado el metodo pop")


def probarTADCola():
  
    q = Queue()
    try:
        print("Probando TAD Cola\n")
        revisarSize(len(q),0)
        print("Se verifico el calclulo de longitud para cola vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarEnqueue(q,0)
        print("Se verifico que el metodo Enqueue funciona cuando la cola es vacia")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(q),1)
        print("Se verifico el calclulo de longitud para cola con un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarEnqueue(q,1)
        print("Se verifico que el metodo Enqueue funciona cuando la cola tiene un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(q),2)
        print("Se verifico el calclulo de longitud para cola con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarDequeue(q)
        print("Se verifico que el metodo Dequeue funciona para cola con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
    except IndexError as e2:
        print("No implementado el metodo Dequeue")

    try:
        revisarDequeue(q)
        print("Se verifico que el metodo Dequeue funciona para cola de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
    except IndexError as e2:
        print("Mal implementado el metodo Dequeue")

    try:
        revisarIsEmpty(q)
        print("Se verifico que el metodo isEmpty funciona correctamente")
    except NoPasaElTest as e:
        print(e.mensaje)
    except IndexError as e2:
        print("Mal implementado el metodo Dequeue")

################################
## Inicio de la Aplicacion
################################

if __name__ == "__main__":
#    numElems = parseArgs(sys.argv)
    probarTADLista()
    probarTADPila()
    probarTADCola()
