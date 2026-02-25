"""
    A doubly linked list implementation using a Node class and......

    Methods: 

    """

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length
    
    def size(self):
        return self.length

    def append(self, val):
        new_node = Node(val)

        if self.head == None: # new list case
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length +=1

    def prepend(self, val):
        new_node = Node(val)

        if self.head == None: # new list case
            self.head = new_node
            self.tail = new_node
        else: 
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length +=1

    def insert(self, index, val):
        new_node = Node(val)
        if index < 0 or index > self.length: # bad index
            return "Index does not exist"
        
        if index == 0: # insert at head
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else: 
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node

        elif index == self.length: #insert at tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else: # insert in middle
            prev_node = self.get(index - 1)
            next_node = prev_node.next

            prev_node.next = new_node
            new_node.prev = prev_node
            
            next_node.prev = new_node
            new_node.next = next_node
        
        self.length +=1

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
            val = self.tail.val
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.length -=1

            return val

    def pop_first(self):
        if self.head == None: # empty list case
            return None
        elif self.head == self.tail: # single element list case
            val = self.head.val
            self.head = None
            self.tail = None
            self.length = 0
            return val
        else: 
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            self.head.prev = None
            self.length -=1
            return old_head.val

    def remove(val):
        pass

    def remove_at(index):
        pass

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        currentIndex = 0
        current= self.head

        while currentIndex != index:
            current = current.next
            currentIndex +=1
        
        return current.val

    def set(self, index, val):
        if index < 0 or index >= self.length:
            return None
        
        currentIndex = 0
        current= self.head

        while currentIndex != index:
            current = current.next
            currentIndex +=1
        
        current.val = val

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0