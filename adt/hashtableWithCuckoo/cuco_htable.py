# Hashing Cuco

class CucoEntry(object):
    def __init__(self, key, string):
        self.next = None
        self.prev = None
        self.key = key
        self.string = string
        
class CucoTable:
    # Metodo que construye nuevo HT al instanciar
    def __init__(self, n):
        self._size = n
        self._arr = [None for x in range(n)]
    
    # Metodo para devolver la longitud    
    def __len__(self):
        return self._size
    
    # Metodo para verificar si algun elemento esta en la tabla
    def __contains__(self, target):
        for i in range(self._size):
            if self._arr[i] is not None and self._arr[i].key == target:
                return True
        return False
            
    # Funcion de hash, metodo multiplicativo recomendado por Knuth
    def h1(self, k):
        return int(self._size*((k*0.180339887) % 1))
    
    # Funcion de hash, metodo de divison    
    def h2(self,k):
        return k % self._size
    
    # Funcion para agregar elementos a la tabla    
    def addCucoHash(self, key, string):
        x = CucoEntry(key, string)
        hash1 = self.h1(key)
        for i in range(1,self._size+1):
            if self._arr[hash1] == None:
                self._arr[hash1] = x
                return
            else:
                x, self._arr[hash1] = self._arr[hash1], x
                if hash1 == self.h1(x.key):
                    hash1 = self.h2(x.key)
                else:
                    hash1 = self.h1(x.key)
    
    # Metodo para eliminar de la tabla segun key    
    def removeHashtable(self, k):
        if self._arr[self.h1(k)] is not None and self._arr[self.h1(k)].key == k:
            item = self._arr[self.h1(k)].string
            self._arr[self.h1(k)] = None
            return item
        if self._arr[self.h2(k)] is not None and self._arr[self.h2(k)].key == k:
            item = self._arr[self.h2(k)].string
            self._arr[self.h2(k)] = None
            return item
        return None
    
    # Metodo para buscar un key en la tabla y retornar el string
    def searchHashtable(self, k):
        if self._arr[self.h1(k)] is not None and self._arr[self.h1(k)].key == k:
            return self._arr[self.h1(k)].string
        if self._arr[self.h2(k)] is not None and self._arr[self.h2(k)].key == k:
            return self._arr[self.h2(k)].string
        return None
        
    # Metodo para buscar un key en la tabla y retornar el string
    def searchHashtableBool(self, k):
        if self._arr[self.h1(k)] is not None and self._arr[self.h1(k)].key == k:
            return True
        if self._arr[self.h2(k)] is not None and self._arr[self.h2(k)].key == k:
            return True
        return False
    
    # Metodo que muetra todos los elementos en la tabla
    def showHashtable(self):
        for i in range(self._size):
            if self._arr[i] is not None:
                print(str(self._arr[i].key) + " " + self._arr[i].string)
        
