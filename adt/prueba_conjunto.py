#!/usr/bin/env python
# Adolfo Jeritson. 12-10523
# Cliente para probar operaciones en TAD conjunto
from conjunto import *

class NoPasaElTest(Exception):
      def __init__(self,mensaje):
          self.mensaje = mensaje

def revisarSize(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("esta calculando mal la longitud")

def revisarPertenece(valorActual,esperado):
    if valorActual != esperado:
        raise NoPasaElTest("el metodo .pertenece no esta funcionando correctamente")

def revisarAdd(lista,elem):
    l = []
    for i in lista:
       l.append(i)
    l.append(elem)
    lista.agregar(elem)
    for i in l:
       if  not i in lista:
          raise NoPasaElTest("el metodo .agregar no esta funcionando correctamente")

def revisarUnion(c1, c2):
    l = []
    for elem in c1:
        l.append(elem)
    for elem in c2:
        l.append(elem)
    c3 = c1.union(c2)
    for i in l:
        if not i in c3:
            raise NoPasaElTest("el metodo .union no esta funcionando correctamente")

def revisarDif(c1, c2):
    l = []
    for elem in c1:
        if not elem in c2:
            l.append(elem)

    c3 = c1.diferencia(c2)
    for i in l:
        if not i in c3:
            raise NoPasaElTest("el metodo .diferencia no esta funcionando correctamente")
            

def probarTADConjunto():
  
    c1 = Conjunto()
    c2 = Conjunto()
    try:
        print("Probando TAD Conjunto\n")
        revisarSize(len(c1),0)
        print("Se verifico el calclulo de longitud para conjunto vacio")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        result = c1.pertenece(1)
        revisarPertenece(result,False)
        print("Se verifico que el metodo .pertenece funciona para vacio")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(c1, 0)
        print("Se verifico que el metodo .agregar funciona cuando es vacio")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        result = c1.pertenece(0)
        revisarPertenece(result,True)
        print("Se verifico que la operacion .pertenece funciona para un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(c1),1)
        print("Se verifico el calclulo de longitud para con un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarAdd(c1,1)
        print("Se verifico que el metodo .agregar funciona cuando se tiene un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        result = c1.pertenece(1)
        revisarPertenece(result,True)
        print("Se verifico que la operacion .pertenece funciona para con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)

    try:
        revisarSize(len(c1),2)
        print("Se verifico el calclulo de longitud para con mas de un elemento")
    except NoPasaElTest as e:
        print(e.mensaje)
    
    c2.agregar(2)
    c2.agregar(3)
    
    try:
        revisarUnion(c1, c2)
        print("Se verifico que el metodo .union funciona")
    except NoPasaElTest as e:
        print(e.mensaje)
    
    c2.agregar(1)
    try:
        revisarDif(c1, c2)
        print("Se verifico que el metodo .diferencia funciona")
    except NoPasaElTest as e:
        print(e.mensaje)
        
    c1.mostrar()
    c2.mostrar()
    
################################
## Inicio de la Aplicacion
################################

if __name__ == "__main__":
    probarTADConjunto()
