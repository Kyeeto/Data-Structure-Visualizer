"""
    A singly linked list implementation using a Node class and keeping track of the head, tail, and length

    Methods: 
    is_empty()        : Return True if the Linked List is empty, False otherwise
    size()            : Returns the length of the Linked List, 0 if empty
    append(val)       : Adds a node with value "val" at the tail of the list
    prepend(val)      : Adds a node with value "val" at the head of the list
    insert(index, val): Insert a node with a value "val" at index
    pop()             : Removes and returns the value of the tail node
    remove(val)       : Removes the first node containing "val" and retuns it, Returns None if not found
    find(val)         : Returns the index of the first node containing "val", Returns "Value not found", if not found
    get(index)        : Returns the value at the given index, Returns "Index does not exist" if out of bounds
    getNode(index)       : Returns the value at the given index, Returns "Index does not exist" if out of bounds 
    clear()           : Removes all nodes from the list
    """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def append(self, val):
        new_node = Node(val)

        if self.head == None: # new list case
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, val):
        new_node = Node(val)

        if self.head == None: # new list case
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, index, val):
        new_node = Node(val)
        if index < 0 or index > self.length: # bad index
            return "Index does not exist"
        
        if index == 0: #insert at head
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node

        elif index == self.length: #insert at tail
            self.tail.next = new_node
            self.tail = new_node

        else:  #insert in middle
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self.length += 1


    def pop(self):
        if self.head == None: # empty list case
            return None
        elif self.head == self.tail: # single element list case
            val = self.head.val
            self.head = None
            self.tail = None
            self.length = 0
            return val
        else: 
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            val = self.tail.val
            current.next = None
            self.tail = current
            self.length -= 1

            return val

    def remove(self, val):
        if self.head == None: # empty list case
            return None
        
        elif self.head.val == val: # removing the head case
            removed_val = self.head.val
            self.head = self.head.next
            if self.head == None: # removed head was only item case
                self.tail = None
            self.length -= 1
            return removed_val
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next

        if current.next == None: # val wasn't found
            return None
        else: 
            removed_val = current.next.val
            current.next = current.next.next

            if current.next == None:
                self.tail = current
        self.length -= 1
        return removed_val

    def find(self, val):
        current = self.head
        index = 0

        while current != None:
            if current.val == val:
                return index
            else:
                current = current.next
                index += 1
        return None
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        currentIndex = 0

        while currentIndex != index:
            current = current.next
            currentIndex += 1
        
        return current.val
    
    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        
        currentIndex = 0
        current = self.head

        while currentIndex != index:
            current = current.next
            currentIndex +=1
        
        return current.val

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0