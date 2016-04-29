# Node class for list
# Adolfo Jeritson. 12-10523
# 2016

class HashEntry(object):
    def __init__(self, key, string):
        self.next = None
        self.prev = None
        self.key = key
        self.string = string
