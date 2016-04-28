
# Implementacion de listas doblemente enlazadas
# Marzo 2016

# Clase que contiene la informacion del elemento (datos satelite)
class HashEntry(object):
    def __init__(self, key, string):
        self.next = None
        self.prev = None
        self.key = key
        self.string = string

class dList:
    # Constructor inicial, el head es none y size cero
    def __init__(self):
        self._head = None
        self._size = 0
    
    # Definimos metodo para retornar size
    def __len__(self):
        return self._size
        
    # Definimos metodo para usar sintaxis x in dList
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and (curNode.key != target and curNode.string != target):
            curNode = curNode.next
        return curNode is not None
    
    # Metodo para mostrar los elementos en la lista
    def showList(self):
        curNode = self._head
        while curNode is not None:
            print(str(curNode.key) + "  =>  " + curNode.string)
            curNode = curNode.next
    
    # Metodo para agregar nuevos elementos a la lista doblemente enlazada
    def add(self, key, st):
        newNode = HashEntry(key, st)
        newNode.next = self._head
        
        if self._head is not None:
            self._head.prev = newNode
            
        self._head = newNode
        self._size += 1
    
    # Metodo para eliminar elementos de la lista
    def remove(self, key):
        curNode = self._head
        if curNode is not None:
            predNode = curNode.prev
        while curNode is not None and curNode.key != key :
            predNode = curNode
            curNode = curNode.next
            
        # The item has to be in the bag to remove it.
        if curNode is None:
            return None
        
        # Unlink the node and return the item.
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
            if self._head is not None:
                self._head.prev = None
        else:
            predNode.next = curNode.next
        return curNode.string
        
    # Metodo para buscar elementos en la lista
    def search(self, key):
        curNode = self._head
        while curNode is not None and curNode.key != key:
            curNode = curNode.next
        if curNode is not None:
            return curNode.string
        else:
            return None
    
    # Metodo para iterar en la lista
    def __iter__(self):
        return ListIterator(self._head)

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
            item = self._curNode.key
            self._curNode = self._curNode.next
            return item

    def prev(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.key
            self._curNode = self._curNode.prev
            return item
    
    
