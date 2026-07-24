class Stack(): 
    """
    A stack (LIFO) implementation using a Python list with the top of the stack being the end of the list

    Methods: 
    __init__        : Initialize an empty list representing the stack. 
    push(val)       : Adds a singular value to the top of the stack if cap is not met
    pop()           : Removes the item from the top of the stack and returns the value. If stack is empty, returns none
    peek()          : Returns the value of the item on the top of the stack without modifying it
    is_empty()      : Returns a True / False value on if the list is empty
    size()          : Returns the number of all of the items in the stack
    clear()         : Removes all items from the stack
    """

    def __init__ (self):
        self.stack = []
        self.cap = 5
        self.length = 0

    def push(self, val):
        if self.length == self.cap:
            return "Stack is Full"
        else: 
            self.length += 1
            self.stack.append(val)

    def pop(self):
        if self.length == 0:
            return None 
        else:
            self.length -= 1
            return self.stack.pop()

    def peek(self): 
        if self.length == 0:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        if self.length == 0: 
            return True
        else: 
            return False
        
    def size(self):
        return self.length
    
    def clear(self):
        self.length = 0
        self.stack.clear()
        
    def __str__(self):
        return str(self.stack)