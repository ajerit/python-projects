#!/usr/bin/env python
#
# Descripcion: Implementacion del TAD Cola usando
#     	       listas enlazadas
#
# Autor: Federico Flaviani
# Autor: Adolfo Jeritson
# 

from linkedList import ListNode, ListIterator

# Descripcion: Clase que implementa una cola usando listas enlazadas
#   Atributos: _qhead: atributo privado que referencia al primer elemento de la cola
#              _qtail: atributo privado que referencia al ultimo elemento de la cola
#              _count: atributo privado entero que indica la longitud de la cola

class Queue:

  def __init__(self):
    self._qhead = None
    self._qtail = None
    self._count = 0

# Descripcion: Metodo que indica si la cola es vacia o no
#     Retorna: booleano que indica si la cola es vacia

  def isEmpty(self):

    return self._count==0

# Descripcion: Metodo que devuelve la longitud de la cola
#     Retorna: entero que indica la longitud de la cola

  def __len__(self):

    return self._count

# Descripcion: Metodo que encola un nuevo elemeto item al final de la cola
#   Atributos: item: elemento a ser encolado a la cola

  def enqueue(self,item):
    
    n = ListNode(item)
    if self.isEmpty():
	  self._qtail = n
	  self._qhead = n
	  
    else:
	  self._qtail.next = n
	  self._qtail = n
	  
    self._count+=1 

# Descripcion: Metodo que desencola la cabeza de la cola
#     Retorna: Si la cola no es vacia se devuelve el elemento
#              desencolado

  def dequeue(self):

    if self.isEmpty():
	  pass
	  
    else:
      self._count-=1
      n = self._qhead
      self._qhead = self._qhead.next
      return n
	  
    

# Descripcion: Metodo que verifica si el elemento target se encuentra
#              en algun nodo de la lista
#   Atributos: target: elemento a ser buscado en la lista
#     Retorna: valor booleano que indica si el elemento esta o no en la lista

  def __contains__(self, target):
    curNode = self._qhead
    while curNode is not None and curNode.data != target:
      curNode = curNode.next
    return curNode is not None


# Descripcion: Metodo que devuelve un iterador de la cola
#     Retorna: iterador de la cola

  def __iter__(self):
    return ListIterator(self._qhead)

