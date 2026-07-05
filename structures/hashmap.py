"""
    A hashmap implementation using chaining for collision handling, built on a fixed-size array of linked nodes

    Methods:
    insert(key, val)  : Adds a key-value pair, updates val if key already exists
    get(key)          : Returns the value associated with key, returns None if not found
    delete(key)       : Removes the key-value pair, returns None if not found
    contains(key)     : Returns True if key exists in the map, False otherwise
    size()            : Returns the number of key-value pairs in the map
    is_empty()        : Returns True if the map is empty, False otherwise
    clear()           : Removes all key-value pairs and resets the map
    """

class Node():
    def __init__(self, key, val, next = None):
        self.val = val
        self.key = key
        self.next = next

class Hashmap():
    def __init__(self):
        self.cap = 10
        self.length = 0
        self.map = [None] * 10

    def hashKey(self, key):
        hash = 0
        for char in key:
            hash = hash * 37 + ord(char)
        return hash % self.cap
    def insert(self, key, val):
        index = self.hashKey(key)
        if (self.map[index] == None):
            self.map[index] = Node(key, val)
            self.length +=1
        else:
            current = self.map[index]
            while current != None:
                if (current.key == key): 
                    current.val = val
                    return
                if (current.next == None):
                    current.next = Node(key, val)
                    self.length +=1 
                    return
                current = current.next

    def delete(self, key):
        index = self.hashKey(key)
        if (self.map[index] == None):
            return None
        if self.map[index].key == key:
            self.map[index] = self.map[index].next
            self.length -=1
            return
        prev = self.map[index]
        current = self.map[index].next
        while (current != None):
            if current.key == key:
                prev.next = current.next
                self.length -=1
                return
            prev = current
            current = current.next
        return None


    def get(self, key):
        index = self.hashKey(key)
        if (self.map[index] == None):
            return None
        current = self.map[index]
        while (current != None):
            if (current.key == key):
                return current.val
            current = current.next
        return None
    
    def contains(self, key):
        return self.get(key) != None

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def clear(self):
        self.map = [None] * 10
        self.length = 0