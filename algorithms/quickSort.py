"""
A Simple Quick Sort implementation. 
"""

def partition(lst, start, end):
    pivot = lst[start]
    low = start + 1
    high = end

    while True:
        while low <= high and lst[high] >= pivot:
            high = high - 1

        while low <= high and lst[low] <= pivot:
            low = low + 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
        else:
            break
    
    lst[start], lst[high] = lst[high], lst[start]

    return high

def quickSort(lst, start, end):
    if start >= end:
        return
    
    p = partition(lst, start, end)
    quickSort(lst, start, p - 1)
    quickSort(lst, p + 1, end)