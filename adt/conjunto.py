# Adolfo Jeritson. 12-10523
# TAD Conjunto 

class ListNode:
    def __init__(self, link, item):
        self._next = link
        self._item = item
        
class Conjunto:
    def __init__(self):
        self._size = 0
        self._head = None
    
    # Funcion para retornar la longitud del conjunto    
    def __len__(self):
        return self._size
        
    # Funcion que me permite iterar sobre el conjunto
    def __iter__(self):
        return ListIterator(self._head)
    
    # Funcion que retorna si el elemento pertenece al conjunto    
    def __contains__(self, item):
        cNode = self._head
        while cNode is not None and cNode._item != item:
            cNode = cNode._next
        return cNode is not None 
    
    # Funcion para agregar nuevos elementos al conjunto
    def agregar(self, item):
        nodo = ListNode(self._head, item)
        self._head = nodo
        self._size += 1
        
    # Funcion que retorna un booleano dependiendo si el elemento esta en
    # en el conjunto
    def pertenece(self, item):
        return item in self
    
    # Implementacion de la operacion union de conjuntos, devuelve un
    # conjunto nuevo con la union
    def union(self, c):
        new = Conjunto()
        for elem in c:
            new.agregar(elem)
        for elem in self:
            new.agregar(elem)
        return new
    
    # Implementacion de la operacion de diferencia de conjuntos, devuelve
    # un conjunto nuevo con la diferencia.    
    def diferencia(self, c):
        new = Conjunto()
        for elem in self:
            if not elem in c:
                new.agregar(elem)
        return new
        
    # Funcion para mostrar los elementos del conjunto
    def mostrar(self):
        print("[ "),
        for elem in self:
            print(str(elem) + " "),
        print("]")
        
# Clase para poder iterar sobre el conjunto
class ListIterator:
  def __init__(self, head):
    self._cNode = head

  def __iter__(self):
    return self

  def next(self):
    if self._cNode is None:
      raise StopIteration
    else :
      item = self._cNode._item
      self._cNode = self._cNode._next
      return item
