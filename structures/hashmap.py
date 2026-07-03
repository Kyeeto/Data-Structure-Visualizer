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

    def delete(key):
        pass

    def get(key):
        pass

    def contains(key):
        pass

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def clear(self):
        self.map = [None] * 10
        self.length = 0