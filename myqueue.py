class Queue(): 
    """
    A simple queue (FIFO) implementation using a Python list with the front of the line being index[0]

    Methods:
    --------
    __init__(maxsize)   : Initialize an empty list representing the queue with a maximum size of maxsize.
    enqueue(val)        : Adds a singular value to the back of the queue. Returns "Queue is full" if the queue is full, 
    dequeue()           : Removes and returns the value at the front of the line. Returns None if empty
    front()             : Return the front value of queue without removing it. Returns None if empty
    is_empty()          : Return True if the queue is empty, False otherwise.
    qsize()             : Return the number of elements in the queue.
    is_full()              : Returns true if the queue has reached its maximum size
    clear()             : Remove all elements from the queue.
    """

    def __init__(self, maxsize):
        self.queue = []
        self.maxsize = maxsize

    def enqueue(self, val):
        if len(self.queue) == self.maxsize:
            return "Queue is Full"
        else:
            self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None 
        else:
            return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0: 
            return True
        else: 
            return False

    def qsize(self): 
        return len(self.queue)

    def is_full(self):
        return len(self.queue) == self.maxsize

    def clear(self):
        self.queue.clear()

    def __str__(self):
        return str(self.queue)
    