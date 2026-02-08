class Stack(): 
    def __init__ (self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return None 
        else:
            val = self.stack[len(self.stack) - 1]
            self.stack.remove(val)
            return val

    def peek(self): 
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if len(self.stack == 0): 
            return True
        else: 
            return False