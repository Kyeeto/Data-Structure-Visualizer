"""
A fixed-capacity array implementation using a Python list pre-allocated with None values

Methods: 
get(index)              : Returns the value at the given index
set(index, val)         : Sets the value at the given indx to "val"
append(val)             : Adds "Val" at the next open position, returns "Array is full" if at capacity 
insert(index, val)      : Inserts "val" at "index" by shifting elements right, returns "Index out of bounds" if invalid
find(val)               : Returns the index of the first occurrence of "val", returns None if not found
contains(val)           : Returns True if "val" exists in the array, False otherwise
size()                  : Returns the number of elements currently in the array
is_empty()              : Returns True if the array has no elements, False otherwise
clear()                 : Removes all elements and resets the array the None values
"""

class MyArray():
    def __init__(self):
        self.cap = 10
        self.length = 0
        self.arr = [None] * 10

    def get(self, index):
        return self.arr[index]

    def set(self, index, val):
        self.arr[index] = val

    def append(self, val):
        if self.length == self.cap:
            return "Array is full"
        self.arr[self.length] = val
        self.length += 1

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return "Index out of bounds"
        if self.length == self.cap:
            return "Array is full"
        for i in range(self.length, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = val
        self.length += 1

    def find(self, val):
        for i in range(self.length):
            if self.arr[i] == val:
                return i
        return None

    def contains(self, val):
        return self.find(val) is not None

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.arr = [None] * self.cap
        self.length = 0