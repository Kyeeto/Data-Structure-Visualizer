"""
A Simple Heap Sort implementation. 
"""

def heap(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lst[i] < lst[l]:
        largest = l
    elif r < n and lst[largest] < lst[r]:
        largest = r
    elif largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heap(lst, n, largest)

def heapSort(lst):
    n = len(lst)

    for i in range(n//2, -1, -1):
        heap(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]

        heap(lst, i, 0)