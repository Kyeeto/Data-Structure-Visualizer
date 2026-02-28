"""
    A doubly linked list implementation using a Node class and keeping track of head, tail, and length

    Methods: 
    is_empty()           : Returns True if the Linked List is empty, False otherwise
    size()               : Returns the length of the Linked List, 0 if empty
    append(val)          : Adds a node with the value "val" at the tail of the list
    prepend(val)         : Adds a node with the value "val" at the head of the list
    insert(index, val)   : Insert a node with a value "val" at index
    pop()                : Removes and returns the value of the tail node
    pop_first()          : Removes and returns the value of the head node
    remove(val)          : Removes the first node containing "val" and returns it, Returns None if not found
    remove_at(index)     : Removess the node at "index" and returns in, Returns None if not found
    find(val)            : Returns the index of the first node containing "val", Returns "Value not found", if not found
    get(index)           : Returns the value at the given index, Returns "Index does not exist" if out of bounds
    getNode(index)       : Returns the value at the given index, Returns "Index does not exist" if out of bounds 
    set(index, val)      : Updates the value with "val" at the node at "index"
    clear()              : Removes all nodes from the list

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
            prev_node = self.getNode(index - 1)
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

    def remove(self, val):
        if self.head == None: #empty list case
            return None
        elif self.head.val == val: #remove head case
            removed_val = self.head
            self.head = self.head.next
            if self.head == None: # head was only item case
                self.tail = None
                self.length = 0
                return removed_val

            self.head.prev = None
            self.length -=1
            return removed_val
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next

        if current.next == None:
            return None
        else: 
            removed_val = current.next
            if current.next == self.tail: #removed tail case
                self.tail = current
                self.tail.next = None
            else: 
                current.next = current.next.next
                current.next.prev = current
            self.length -=1
            return removed_val
        
    def remove_at(self, index):
        if index < 0 or index >= self.length:
            return None
        
        currentIndex = 0
        current = self.head
        while currentIndex != index:
            current = current.next
            currentIndex +=1
        removed_index = current

        if index == 0: # remove head case
            self.head = self.head.next
            if self.head == None: # head was only item case:
                self.tail = None
                self.length = 0
                return removed_index
            
            self.head.prev = None
            self.length -=1
            return removed_index
        
        elif index == self.length - 1: # remove tail case
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -=1
            return removed_index
        
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -=1
            return removed_index

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
        
        currentIndex = 0
        current = self.head

        while currentIndex != index:
            current = current.next
            currentIndex +=1
        
        return current.val
    
    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        
        currentIndex = 0
        current = self.head

        while currentIndex != index:
            current = current.next
            currentIndex +=1
        
        return current

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