# Clase para los nodos de la listas de la tabla
# Adolfo Jeritson. 12-10523

class HashEntry(object):
    def __init__(self, key, string):
        self.next = None
        self.prev = None
        self.key = key
        self.string = string
