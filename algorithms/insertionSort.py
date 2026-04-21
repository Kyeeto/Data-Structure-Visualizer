"""
A Simple Insertion Sort implementation. 
"""

def insertionSort(lst):
    steps = []
    arr = lst[:]

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        steps.append({
                "array" : arr[:],
                "key_index" : i,
                "comparing" : j, 
                "swapped" : False
            })
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            steps.append({
                "array" : arr[:],
                "key_index" : j,
                "comparing" : j, 
                "swapped" : False
            })
            j -= 1
        lst[j + 1] = key
        steps.append({
                "array" : arr[:],
                "key_index" : j + 1,
                "comparing" : j + 1, 
                "swapped" : False
            })
        
    return steps