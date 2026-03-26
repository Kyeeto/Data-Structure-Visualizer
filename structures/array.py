class MyArray(): 
    def __init__(self, cap):
        self.cap = cap
        self.length = self.length
        self.arr = [None] * cap

    def get(self, index):
        return self.arr[index]

    def set(self, index, val):
        self.arr[index] = val

    def append(self, val):
        if self.length == self.cap:
            return "Array is full"
        else:
            self.arr.append(val)

    def insert(index, val):
        pass

    def find(val):
        pass

    def contains(val):
        pass

    def size():
        pass

    def is_empty():
        pass

    def clear():
        pass